#!/usr/bin/env python3.6

import csv

FIELDNAMES = (
    'id',
    'title',
    'text',
    'iso2',
    'valid_date',
)

WEEKDAYS_LONG = (
    'Montag',
    'Dienstag',
    'Mittwoch',
    'Donnerstag',
    'Freitag',
    'Samstag',
    'Sonntag',
)

WEEKDAYS_SHORT = (
    'MO',
    'DI',
    'MI',
    'DO',
    'FR',
    'SA',
    'SO',
)


def clean_up_texts(input_filepath, output_filepath):
    written_rows = 0

    with open(input_filepath) as input_file, open(
            output_filepath, 'w') as output_file:
        reader = csv.DictReader(input_file, delimiter=';')
        writer = csv.DictWriter(
            output_file, fieldnames=FIELDNAMES, delimiter=';')
        for row in reader:
            if is_valid(row):
                row['text'] = extract_relevant_text(row['title'], row['text'])
                writer.writerow(row)
                written_rows += 1

    print('Wrote %s rows to "%s"' % (written_rows, output_filepath))


def covers_another_weekday(line, target_weekday, num_tokens=5):
    '''
    Returns ``True`` if one of the non-target weekday names appears within
    the first ``num_tokens`` tokens of ``line``.
    '''
    other_weekdays = set(WEEKDAYS_LONG)
    other_weekdays.remove(target_weekday)

    line_set = set(line.split()[:num_tokens])

    if other_weekdays & line_set:
        return True

    return False


def determine_target_weekday(title):
    # Check for full weekday names first
    for weekday in WEEKDAYS_LONG:
        if weekday in title:
            return weekday

    for i, weekday_short in enumerate(WEEKDAYS_SHORT):
        if weekday_short in title:
            return WEEKDAYS_LONG[i]

    raise BaseException(
        f'Unable to determine target weekday from title "{title}"')


def extract_relevant_text(title, text):
    relevant_lines = []

    target_weekday = determine_target_weekday(title)

    # Detect pattern to remove overview line
    # ['teaser', 'blank', 'line', 'blank']
    overview_pattern = []

    for line in text.splitlines():
        # Remove overview line
        if overview_pattern == ['teaser', 'blank', 'line', 'blank']:
            relevant_lines.pop()

        line = line.strip()

        if line.startswith(WEEKDAYS_SHORT):
            overview_pattern = ['teaser']
        elif line:
            overview_pattern.append('line')
        else:
            overview_pattern.append('blank')
            continue

        # As soon as a line covers another weekday, ignore the remaining text
        if covers_another_weekday(line, target_weekday):
            break

        if is_relevant(line):
            relevant_lines.append(line)

    return '\n'.join(relevant_lines)


def is_relevant(line):
    # Let's ignore titles within the text (there's a separate title column)
    if line.startswith('Vorhersage für'):
        return False

    return True


def is_valid(row):
    if row['text'].startswith('Test'):
        return False

    return True


if __name__ == '__main__':
    clean_up_texts(
        'data/weather_reports.csv', 'data/weather_reports_clean.csv')

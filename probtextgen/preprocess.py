import csv

FIELDNAMES = [
    'id',
    'title',
    'text',
    'iso2',
    'valid_date'
]


def clean_up_texts(input_filepath, output_filepath):
    written_rows = 0

    with open(input_filepath) as input_file, open(
            output_filepath, 'w') as output_file:
        reader = csv.DictReader(input_file, delimiter=';')
        writer = csv.DictWriter(
            output_file, fieldnames=FIELDNAMES, delimiter=';')
        for i, row in enumerate(reader):
            # TODO: Remove
            print(row)
            if is_valid(row):
                writer.writerow(row)
                written_rows += 1
            # TODO: Remove
            if i > 4:
                break

    print('Wrote %s rows to "%s"' % (written_rows, output_filepath))


def is_valid(row):
    if row['text'].startswith('Test'):
        return False

    return True


if __name__ == '__main__':
    clean_up_texts(
        'data/weather_reports.csv', 'data/weather_reports_clean.csv')

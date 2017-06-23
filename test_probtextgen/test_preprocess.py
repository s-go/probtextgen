from collections import OrderedDict

import pytest

from probtextgen.preprocess import covers_another_weekday
from probtextgen.preprocess import determine_target_weekday
from probtextgen.preprocess import extract_relevant_text
from probtextgen.preprocess import is_valid


@pytest.fixture
def extracted_text():
    with open('test_probtextgen/fixtures/extracted_text.txt') as file:
        return file.read()


@pytest.fixture
def original_text():
    with open('test_probtextgen/fixtures/original_text.txt') as file:
        return file.read()


class TestPreprocess:

    def test_covers_another_weekday(self):
        target_weekday = 'Sonntag'

        assert (
            covers_another_weekday(
                'Der Sonntag beginnt von Westen her sonnig', target_weekday)
            is False
        )

        assert (
            covers_another_weekday(
                'In der Nacht zum Dienstag frischt der Ostwind weiter auf',
                target_weekday)
            is True
        )

    def test_determine_target_weekday(self):
        assert (
            determine_target_weekday(
                'Vorhersage für Bayern, Sonntag, 13.03.2016') == 'Sonntag'
        )

        assert (
            determine_target_weekday(
                'Vorhersage für Bayern, SO, 13.03.2016') == 'Sonntag'
        )

    def test_extract_relevant_text(self, original_text, extracted_text):
        title = 'Vorhersage für Bayern, Sonntag, 13.03.2016'

        assert (
            extract_relevant_text(title, original_text) == extracted_text
        )

    def test_is_valid(self):
        invalid_rows = [
            OrderedDict([
                ('id', '3197'),
                ('title', 'Test Rheinland-Pfalz'),
                ('text', 'Test Eintrag Rheinland-Pfalz für 2015-12-07'),
                ('iso2', 'DE-RL'),
                ('valid_date', '2015-12-07')
            ])
        ]

        for row in invalid_rows:
            assert is_valid(row) is False

        valid_rows = [
            OrderedDict([
                ('id', '3197'),
                ('title', 'Rheinland-Pfalz'),
                ('text', 'Eintrag Rheinland-Pfalz für 2015-12-07'),
                ('iso2', 'DE-RL'),
                ('valid_date', '2015-12-07')
            ])
        ]

        for row in valid_rows:
            assert is_valid(row) is True

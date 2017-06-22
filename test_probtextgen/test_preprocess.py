from collections import OrderedDict
import unittest

from probtextgen.preprocess import covers_another_weekday
from probtextgen.preprocess import extract_relevant_text
from probtextgen.preprocess import is_valid


class TestPreprocess(unittest.TestCase):

    def test_covers_another_weekday(self):
        target_weekday = 'Sonntag'

        self.assertFalse(
            covers_another_weekday(
                'Der Sonntag beginnt von Westen her sonnig', target_weekday))

        self.assertTrue(
            covers_another_weekday(
                'In der Nacht zum Dienstag frischt der Ostwind weiter auf',
                target_weekday))

    def test_extract_relevant_text(self):
        title = 'Vorhersage für Bayern, Sonntag, 13.03.2016'
        text = '''Vorhersage für Bayern, Sonntag, 13.03.2016

SO: Nachtfrost, meist bewölkt, bis 7°C, Ostwind.

An der Ostflanke einer Hochdruckbrücke über Miitteleuropa fliesst weiter kühlere Luft heran. Der Hochdruckeinfluss hält voraussichtlich bis Donnerstag an.

In der Nacht zum Sonntag nimmt der Wind aus östlichen Richtungen zu, und wird dabei böiger, die Hochnebelfelder verdichten sich und die Temperaturen sinken bis 0°C  in den Ebenen, und -2°C am Alpenrand.
Der Sonntag beginnt von Westen her sonnig, die Hochnebelfelder lösen sich auch teils im Osten und die Temperaturen steigen bis 7°C in den Ebenen und Null Grad auf 1200 Metern Höhe bei zeitweise starkem, böigem Wind aus östlichen Richtungen.
Nachts lässt der Wind etwas nach, und es gibt verbreitet leichten Frost.
Am Montag frischt der Ostwind wieder auf bei Temperaturen bis  maximal 5°C und auflockernder Bewölkung, teils mit Sonne.
In der Nacht zum Dienstag frischt der Ostwind weiter auf und die Temperaturen erreichen bis 7°C in Franken, und 3°C in Niederbayern und am Alpenrand.
Der Mittwoch bringt Sonne, höhere Temperaturen bis 10°C und abnehmender Wind aus Süd.
'''
        self.assertEqual(
            extract_relevant_text(title, text),
            '''SO: Nachtfrost, meist bewölkt, bis 7°C, Ostwind.
In der Nacht zum Sonntag nimmt der Wind aus östlichen Richtungen zu, und wird dabei böiger, die Hochnebelfelder verdichten sich und die Temperaturen sinken bis 0°C  in den Ebenen, und -2°C am Alpenrand.
Der Sonntag beginnt von Westen her sonnig, die Hochnebelfelder lösen sich auch teils im Osten und die Temperaturen steigen bis 7°C in den Ebenen und Null Grad auf 1200 Metern Höhe bei zeitweise starkem, böigem Wind aus östlichen Richtungen.
Nachts lässt der Wind etwas nach, und es gibt verbreitet leichten Frost.''')

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
            self.assertFalse(is_valid(row))

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
            self.assertTrue(is_valid(row))

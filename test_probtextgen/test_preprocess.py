import unittest

from probtextgen.preprocess import is_valid


class TestPreprocess(unittest.TestCase):

    def test_is_valid(self):
        invalid_rows = [
            {
                'text': 'Test Eintrag Rheinland-Pfalz f\xc3\xbcr 2015-12-07',
                'iso2': 'DE-RL',
                'valid_date': '2015-12-07',
                'id': '3197',
                'title': 'Test Rheinland-Pfalz'
            }
        ]

        for row in invalid_rows:
            self.assertFalse(is_valid(row))

        valid_rows = [
            {
                'text': 'Eintrag Rheinland-Pfalz f\xc3\xbcr 2015-12-07',
                'iso2': 'DE-RL',
                'valid_date': '2015-12-07',
                'id': '3197',
                'title': 'Rheinland-Pfalz'
            }
        ]

        for row in valid_rows:
            self.assertTrue(is_valid(row))


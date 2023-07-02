# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=trailing-newlines
# pylint: disable=trailing-whitespace
# pylint: disable=missing-final-newline

import unittest
from translator import englishToFrench, frenchToEnglish
class TestTranslateMethod(unittest.TestCase):

    def test_engToFr(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertNotEqual(englishToFrench("July"), "Jatems")

    def test_FrToEn(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hi")
        self.assertNotEqual(englishToFrench("Winter"), "Yametai") 

if __name__ == '__main__':
    unittest.main()   
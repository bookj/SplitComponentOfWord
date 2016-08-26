import unittest
from thws.analyzers import meter

class StripingSpecialCharacterTest(unittest.TestCase):

    def setUp(self):
        self.az = meter.MeterAnalyzer()

    def test_given_words_should_strip_exclamation(self):
        words = ['การ', '!']
        output = ['การ']

        result = self.az.strip_special_character(words)
        self.assertEqual(result, output)

    def test_given_word_should_strip_question_mark(self):
        word = ['ถึง', 'ม้วย', 'ดิน', 'สิ้น', 'ฟ้า', 'มหาสมุทร', '?']
        output = ['ถึง', 'ม้วย', 'ดิน', 'สิ้น', 'ฟ้า', 'มหาสมุทร']

        result = self.az.strip_special_character(word)
        self.assertEqual(result, output)

    def test_given_word_should_strip_space(self):
        word = ['ไม่', 'สิ้น', ' ', 'สุด', 'ความ', ' ', 'รัก', 'สมัคร', 'สมาน']
        output = ['ไม่', 'สิ้น', 'สุด', 'ความ', 'รัก', 'สมัคร', 'สมาน']

        result = self.az.strip_special_character(word)
        self.assertEqual(result, output)


    def test_given_word_should_strip_english_alphabet(self):
        word = ['ไม่', 'สิ้น', 'สุดalwaysความ', 'รักasdfwสมัครgoneสมาน']
        output = ['ไม่', 'สิ้น', 'สุด', 'ความ', 'รัก', 'สมัคร', 'สมาน']

        result = self.az.strip_special_character(word)
        self.assertEqual(result, output)



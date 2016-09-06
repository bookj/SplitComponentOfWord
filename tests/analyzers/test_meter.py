import unittest
from thws.analyzers import meter

class SeparateWords(unittest.TestCase):

    def setUp(self):
        self.az = meter.MeterAnalyzer()

    def test_given_sunthorn_phu_sentence_1(self):
        sentence = ("ถึงม้วยดินสิ้นฟ้ามหาสมุทร")
        output = ["ถึง", "ม้วย", "ดิน", "สิ้น", "ฟ้า", "มหาสมุทร"]

        result = self.az.separate_word(sentence)
        self.assertEqual(result, output)

    def test_given_sunthorn_phu_sentence_2(self):
        sentence = ("ไม่สิ้นสุดความรักสมัครสมาน")
        output = ["ไม่", "สิ้น", "สุด", "ความ", "รัก", "สมัคร", "สมาน"]

        result = self.az.separate_word(sentence)
        self.assertEqual(result, output)


class StripingSpecialCharacterTest(unittest.TestCase):

    def setUp(self):
        self.az = meter.MeterAnalyzer()

    def test_given_words_should_strip_exclamation(self):
        words = ('การ!')
        output = ('การ')

        result = self.az.strip_special_character(words)
        self.assertEqual(result, output)

    def test_given_word_should_strip_question_mark(self):
        word = ("ถึงม้วยดินสิ้นฟ้ามหาสมุทร์?")
        output = ("ถึงม้วยดินสิ้นฟ้ามหาสมุทร์")

        result = self.az.strip_special_character(word)
        self.assertEqual(result, output)

    def test_given_word_should_strip_space(self):
        word = ("ไม่สิ้นสุด ความรัก สมัครสมาน")
        output = ("ไม่สิ้นสุดความรักสมัครสมาน")

        result = self.az.strip_special_character(word)
        self.assertEqual(result, output)


    def test_given_word_should_strip_english_alphabet(self):
        word = ("ไม่สิ้นสุดalwaysความรักasdfwสมัครgoneสมาน")
        output = ("ไม่สิ้นสุดความรักสมัครสมาน")

        result = self.az.strip_special_character(word)
        self.assertEqual(result, output)

    def test_given_word_should_strip_new_line(self):
        word = ("บัตรอนุญาติเข้าห้อง\nปฏิบัติการ")
        output = ("บัตรอนุญาติเข้าห้องปฏิบัติการ")

        result = self.az.strip_special_character(word)
        self.assertEqual(result, output)

    def test_given_word_should_strip_tab(self):
        word = ("บัตรอนุญาติเข้าห้อง\tปฏิบัติ\tการ")
        output = ("บัตรอนุญาติเข้าห้องปฏิบัติการ")

        result = self.az.strip_special_character(word)
        self.assertEqual(result, output)

    def test_given_word_should_strip_full_stop(self):
        word = ("บัตรอนุญาติเข้าห้องปฏิบัติการ.")
        output = ("บัตรอนุญาติเข้าห้องปฏิบัติการ")

        result = self.az.strip_special_character(word)
        self.assertEqual(result, output)


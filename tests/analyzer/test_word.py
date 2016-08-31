import unittest

from thws.analyzer.word import WordAnalyzer
# from thws.types import Consonant, Syllable, ConsonantTone
from thws.types import *


class WordAnalyzerTest(unittest.TestCase):

    def split_tone_mark_1_test(self):
        wa = WordAnalyzer()
        word = 'การ'
        kan_consonant = Consonant('ก', 'ก', ConsonantTone.middle)
        result = wa.get_initial(word)

        self.assertEqual(result.format, kan_consonant.format)
        self.assertEqual(result.phonetic, kan_consonant.phonetic)
        self.assertEqual(result.tone, kan_consonant.tone)

    def split_tone_mark_2_test(self):
        wa = WordAnalyzer()
        word = 'เมีย'
        word_vowel = Vowel('เอีย', 'long')
        result = wa.get_nucleus(word)

        self.assertEqual(result.format, word_vowel.format)
        self.assertEqual(result.type, word_vowel.type)

    def split_tone_mark_3_test(self):
        wa = WordAnalyzer()
        word = 'โต๊ะ'
        word_vowel = Vowel('โอะ', 'short')
        result = wa.get_nucleus(word)

        self.assertEqual(result.format, word_vowel.format)
        self.assertEqual(result.type, word_vowel.type)

    def split_tone_mark_4_test(self):
        wa = WordAnalyzer()
        word = 'เสียง'
        final_consonant = Consonant('ง', 'ง')
        result = wa.get_coda(word)

        self.assertEqual(result.format, final_consonant.format)
        self.assertEqual(result.phonetic, final_consonant.phonetic)

    def split_tone_mark_5_test(self):
        wa = WordAnalyzer()
        word = 'ภาพ'
        final_consonant = Consonant('พ', 'บ')
        result = wa.get_coda(word)

        self.assertEqual(result.format, final_consonant.format)
        self.assertEqual(result.phonetic, final_consonant.phonetic)

    def split_tone_mark_6_test(self):
        wa = WordAnalyzer()
        word = 'สวย'
        word_vowel = Vowel('อัว', 'long')
        result = wa.get_nucleus(word)

        self.assertEqual(result.format, word_vowel.format)
        self.assertEqual(result.type, word_vowel.type)

    def split_tone_mark_7_test(self):
        wa = WordAnalyzer()
        word = 'เด็ก'
        word_vowel = Vowel('เอะ', 'short')
        result = wa.get_nucleus(word)

        self.assertEqual(result.format, word_vowel.format)
        self.assertEqual(result.type, word_vowel.type)

# class SplitFirstConsonantTest(unittest.TestCase):
#
#     def split_first_consonant_1_test(self):
#         assert split_component_of_word('หมา').find_first_consonant() == 'หม'

# class SplitVowelTest(unittest.TestCase):

#     def split_vowel_0_test(self):
#         assert split_component_of_word('ใส่').find_vowel() == 'ใอ'

# class SplitFinalConsonantTest(unittest.TestCase):

#     def split_final_consonant_5_test(self):
#         assert split_component_of_word('').findFinalConsonant() == ''

import unittest

from thws.analyzers.word import WordAnalyzer
from thws.types import Consonant, Syllable, ConsonantTone


class WordAnalyzerTest(unittest.TestCase):

    def split_tone_mark_1_test(self):
        wa = WordAnalyzer()
        word = 'การ'
        kan_consonant = Consonant('ก', 'ก', ConsonantTone.middle)
        result = wa.get_initial(word)

        self.assertEqual(result.format, kan_consonant.format)
        self.assertEqual(result.phonetic, kan_consonant.phonetic)
        self.assertEqual(result.tone, kan_consonant.tone)

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

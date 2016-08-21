import unittest

from thws.analyzer.word import WordAnalyzer
# from ..thws.types import Consonant, Syllable


class WordAnalyzerTest(unittest.TestCase):

    def split_tone_mark_1_test(self):
        assert WordAnalyzer().get_initial('กาว') == ['ก', 'ก', 1]
        # assert WordAnalyzer().get_initial('กาว') == Consonant('ก', 'ก', 1)

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

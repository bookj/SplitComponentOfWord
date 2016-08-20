import unittest

from thws.analyzer.word import WordAnalyzer

class SplitToneMarkTest(unittest.TestCase):

    def split_tone_mark_1_test(self):
        assert split_component_of_word('เหมา').find_tone_mark() == None # สามัญ

    def split_tone_mark_2_test(self):
        assert split_component_of_word('เข่า').find_tone_mark() == '\u0E48' # เอก

    def split_tone_mark_3_test(self):
        assert split_component_of_word('เกลี้ยง').find_tone_mark() == '\u0E49' # โท

    def split_tone_mark_4_test(self):
        assert split_component_of_word('เบี๊ยว').find_tone_mark() == '\u0E4A' # ตรี

    def split_tone_mark_5_test(self):
        assert split_component_of_word('เต๋า').find_tone_mark() == '\u0E4B' # จัตวา

class SplitFirstConsonantTest(unittest.TestCase):

    def split_first_consonant_1_test(self):
        assert split_component_of_word('หมา').find_first_consonant() == 'หม'

    def split_first_consonant_2_test(self):
        assert split_component_of_word('ควาย').find_first_consonant() == 'คว'

    def split_first_consonant_3_test(self):
        assert split_component_of_word('เกลี้ยง').find_first_consonant() == 'กล'

    def split_first_consonant_4_test(self):
        assert split_component_of_word('อย่าง').find_first_consonant() == 'อย'

    def split_first_consonant_5_test(self):
        assert split_component_of_word('แหวน').find_first_consonant() == 'หว'

    '''
    def split_first_consonant_0_test(self):
        assert split_component_of_word('').find_first_consonant() == ''
    '''

class SplitVowelTest(unittest.TestCase):

    def split_vowel_1_test(self):
        assert split_component_of_word('เมีย').find_vowel() == 'เอีย'

    def split_vowel_2_test(self):
        assert split_component_of_word('เกลี้ยง').find_vowel() == 'เอีย'

    def split_vowel_3_test(self):
        assert split_component_of_word('โต๊ะ').find_vowel() == 'โอะ'

    def split_vowel_4_test(self):
        assert split_component_of_word('เกาะ').find_vowel() == 'เอาะ'

    def split_vowel_5_test(self):
        assert split_component_of_word('กลัว').find_vowel() == 'อัว'

    def split_vowel_6_test(self):
        assert split_component_of_word('ไฟ').find_vowel() == 'ไอ'

    def split_vowel_7_test(self):
        assert split_component_of_word('ดู').find_vowel() == 'อู'

    def split_vowel_0_test(self):
        assert split_component_of_word('ใส่').find_vowel() == 'ใอ'

    '''
    def split_vowel_0_test(self):
        assert split_component_of_word('').find_vowel() == ''
    '''
'''
class SplitFinalConsonantTest(unittest.TestCase):

    def split_final_consonant_1_test(self):
        assert split_component_of_word('เกลี้ยง').findFinalConsonant() == 'ง'

    def split_final_consonant_2_test(self):
        assert split_component_of_word('หมา').findFinalConsonant() == None

    def split_final_consonant_3_test(self):
        assert split_component_of_word('ปลั๊ก').findFinalConsonant() == 'ก'

    def split_final_consonant_4_test(self):
        assert split_component_of_word('แขวน').findFinalConsonant() == 'น'

    def split_final_consonant_5_test(self):
        assert split_component_of_word('คว้าง').findFinalConsonant() == 'ง'

    def split_final_consonant_5_test(self):
        assert split_component_of_word('').findFinalConsonant() == ''
'''

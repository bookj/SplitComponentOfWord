import unittest

from thai_pronunciation.split_component import split_component_of_word

# class AddTest(unittest.TestCase):
#
#     def add_1_1_should_be_2_test(self):
#         assert add(1,1) == 2


class SplitToneMarkTest(unittest.TestCase):

    def split_tone_mark_1_test(self):
        assert split_component_of_word('เหมา').find_tone_mark() == None

    def split_tone_mark_2_test(self):
        assert split_component_of_word('เข่า').find_tone_mark() == '่'

    def split_tone_mark_3_test(self):
        assert split_component_of_word('เกลี้ยง').find_tone_mark() == '้'

    def split_tone_mark_4_test(self):
        assert split_component_of_word('เบี๊ยว').find_tone_mark() == '๊'

    def split_tone_mark_5_test(self):
        assert split_component_of_word('เต๋า').find_tone_mark() == '๋'

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
        assert split_component_of_word('เมีย').find_vowel() == 'เีย'

    def split_vowel_2_test(self):
        assert split_component_of_word('เกลี้ยง').find_vowel() == 'เีย'

    def split_vowel_3_test(self):
        assert split_component_of_word('โต๊ะ').find_vowel() == 'โะ'

    def split_vowel_4_test(self):
        assert split_component_of_word('เกาะ').find_vowel() == 'เาะ'

    def split_vowel_5_test(self):
        assert split_component_of_word('กลัว').find_vowel() == 'ัว'

    def split_vowel_6_test(self):
        assert split_component_of_word('ไฟ').find_vowel() == 'ไ'

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

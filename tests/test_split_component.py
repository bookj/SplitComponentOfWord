import unittest

from thai_pronunciation.split_component import SplitComponentOfWord

# class AddTest(unittest.TestCase):
#
#     def add_1_1_should_be_2_test(self):
#         assert add(1,1) == 2


class SplitToneMarkTest(unittest.TestCase):

    def split_tone_mark_1_test(self):
        assert SplitComponentOfWord('เหมา').findToneMark() == None

    def split_tone_mark_2_test(self):
        assert SplitComponentOfWord('เข่า').findToneMark() == '่'

    def split_tone_mark_3_test(self):
        assert SplitComponentOfWord('เกลี้ยง').findToneMark() == '้'

    def split_tone_mark_4_test(self):
        assert SplitComponentOfWord('เบี๊ยว').findToneMark() == '๊'

    def split_tone_mark_5_test(self):
        assert SplitComponentOfWord('เต๋า').findToneMark() == '๋'

class SplitFirstConsonantTest(unittest.TestCase):

    def split_first_consonant_1_test(self):
        assert SplitComponentOfWord('หมา').findFirstConsonant() == 'หม'

    def split_first_consonant_2_test(self):
        assert SplitComponentOfWord('ควาย').findFirstConsonant() == 'คว'

    def split_first_consonant_3_test(self):
        assert SplitComponentOfWord('เกลี้ยง').findFirstConsonant() == 'กล'

    def split_first_consonant_4_test(self):
        assert SplitComponentOfWord('อย่าง').findFirstConsonant() == 'อย'

    def split_first_consonant_5_test(self):
        assert SplitComponentOfWord('แหวน').findFirstConsonant() == 'หว'

    '''
    def split_first_consonant_0_test(self):
        assert SplitComponentOfWord('').findFirstConsonant() == ''
    '''

class SplitVowelTest(unittest.TestCase):

    def split_vowel_1_test(self):
        assert SplitComponentOfWord('เมีย').find_vowel() == 'เีย'

    def split_vowel_2_test(self):
        assert SplitComponentOfWord('เกลี้ยง').find_vowel() == 'เีย'

    def split_vowel_3_test(self):
        assert SplitComponentOfWord('โต๊ะ').find_vowel() == 'โะ'

    def split_vowel_4_test(self):
        assert SplitComponentOfWord('เกาะ').find_vowel() == 'เาะ'

    def split_vowel_5_test(self):
        assert SplitComponentOfWord('กลัว').find_vowel() == 'ัว'

    def split_vowel_6_test(self):
        assert SplitComponentOfWord('ไฟ').find_vowel() == 'ไ'

    '''
    def split_vowel_0_test(self):
        assert SplitComponentOfWord('').find_vowel() == ''
    '''
'''
class SplitFinalConsonantTest(unittest.TestCase):

    def split_final_consonant_1_test(self):
        assert SplitComponentOfWord('เกลี้ยง').findFinalConsonant() == 'ง'

    def split_final_consonant_2_test(self):
        assert SplitComponentOfWord('หมา').findFinalConsonant() == None

    def split_final_consonant_3_test(self):
        assert SplitComponentOfWord('ปลั๊ก').findFinalConsonant() == 'ก'

    def split_final_consonant_4_test(self):
        assert SplitComponentOfWord('แขวน').findFinalConsonant() == 'น'

    def split_final_consonant_5_test(self):
        assert SplitComponentOfWord('คว้าง').findFinalConsonant() == 'ง'

    def split_final_consonant_5_test(self):
        assert SplitComponentOfWord('').findFinalConsonant() == ''
'''

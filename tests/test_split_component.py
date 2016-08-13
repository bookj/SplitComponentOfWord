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
    
'''
class SplitVowelTest(unittest.TestCase):

    def split_vowel_1_test(self):
        assert SplitComponentOfWord('').findFirstConsonant() == ''

    def split_vowel_2_test(self):
        assert Calculator("1+1").split_by_plus() == ['1','1']

    def split_vowel_3_test(self):
        assert Calculator("1+1").split_by_plus() == ['1','1']

    def split_vowel_4_test(self):
        assert Calculator("1+1").split_by_plus() == ['1','1']

    def split_vowel_5_test(self):
        assert Calculator("1+1").split_by_plus() == ['1','1']

class SplitFinalConsonantTest(unittest.TestCase):

    def split_final_consonant_1_test(self):
        assert Calculator("1+1").split_by_plus() == ['1','1']

    def split_final_consonant_2_test(self):
        assert Calculator("1+1").split_by_plus() == ['1','1']

    def split_final_consonant_3_test(self):
        assert Calculator("1+1").split_by_plus() == ['1','1']

    def split_final_consonant_4_test(self):
        assert Calculator("1+1").split_by_plus() == ['1','1']

    def split_final_consonant_5_test(self):
        assert Calculator("1+1").split_by_plus() == ['1','1']
'''

from ..types import Consonant, Syllable

class WordAnalyzer:
    def __init__(self):
        pass

    def process(self, text):
        # เช็ค พยัญชนะ สระ ตัวสะกด
        # text = 'การบ้าน'
        pronunciations = []

        s1 = Syllable('การ',
                initial = self.get_initial('การ'))
        s2 = Syllable()
        # check
        pronunciations.append(s1)
        pronunciations.append(s2)

        # return Word(text, pronunciations)

    def get_coda(self, character):
        if character in ['ง']:
            return Consonant(character, 'ง')
        elif character in ['ม']:
            return Consonant(character, 'ม')
        elif character in ['ย']:
            return Consonant(character, 'ย')
        elif character in ['ว']:
            return Consonant(character, 'ว')
        elif character in ['ก', 'ข', 'ค', 'ฆ']:
            return Consonant(character, 'ก')
        elif character in ['บ', 'ป', 'พ', 'ภ', 'ฟ']:
            return Consonant(character, 'บ')
        elif character in ['น', 'ณ', 'ญ', 'ร', 'ล', 'ฬ']:
            return Consonant(character, 'น')
        elif character in ['จ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'ฎ', 'ฏ', 'ฑ', 'ฒ', 'ช', 'ซ', 'ศ', 'ษ', 'ส']:
            return Consonant(character, 'ด')

    def get_initial(self, word):
        ['ก', 'ง', 'จ', 'ฉ', 'ซ', 'บ', 'ป', 'ผ', 'ฝ', 'ฟ', 'ม', 'ร', 'ว', 'ห', 'อ', 'ฮ']
        ['ข', 'ฃ']
        ['ค', 'ฅ', 'ฆ']
        ['ช', 'ฌ']
        ['ย', 'ญ']
        ['ด', 'ฎ']
        ['ต', 'ฏ']
        ['ท', 'ธ', 'ฑ', 'ฒ']
        ['ถ', 'ฐ']
        ['น', 'ณ']
        ['พ', 'ภ']
        ['ล', 'ฬ']
        ['ส', 'ศ', 'ษ']

        middle_character = ['ก', 'จ', 'ฎ', 'ฏ', 'ด', 'ต', 'บ', 'ป', 'อ']
        high_character = ['ข', 'ฃ', 'ฉ', 'ฐ', 'ถ', 'ผ', 'ฝ', 'ศ', 'ษ', 'ส', 'ห']
        pair_low_character = ['ค', 'ฅ', 'ฆ', 'ช', 'ซ', 'ฌ', 'ฑ', 'ฒ', 'ท', 'ธ', 'พ', 'ฟ', 'ภ', 'ฮ']
        single_low_character = ['ง', 'ญ', 'ณ', 'น', 'ม', 'ย', 'ร', 'ล', 'ว', 'ฬ']

        return Consonant( _format, phonetic, tone)

        return 'ก'

    '''
    # มาตราตัวสะกด
    kk = ['ก', 'ข', 'ค', 'ฆ']
    kd = ['จ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'ฎ', 'ฏ', 'ฑ', 'ฒ', 'ช', 'ซ', 'ศ', 'ษ', 'ส']
    kb = ['บ', 'ป', 'พ', 'ภ', 'ฟ']
    kng = ['ง']
    kn = ['น', 'ณ', 'ญ', 'ร', 'ล', 'ฬ']
    km - ['ม']
    ky = ['ย']
    kw = ['ว']
    '''

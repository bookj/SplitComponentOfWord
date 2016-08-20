from ..types import Consonant, Syllable

class WordAnalyzer:
    def __init__(self):
        pass

    def process(self, text):
        # เช็ค พยัญชนะ สระ ตัวสะกด
        # text = 'การบ้าน'
        pronunciations = []
        '''
        s1 = Syllable('การ',
                initial = self.get_initial('การ'),
                medial = None,
                nucleus = None,
                coda = None,
                tone = None,
                _type = None)
        s2 = Syllable()
        '''
        # check
        pronunciations.append(s1)
        pronunciations.append(s2)

        # return Word(text, pronunciations)


    def get_diphthong(self): # คำควบกล้ำ
        regex = r"[^ห|ก-ร|ล|ว-ฮ][ร|ล|ว]"
        match = re.search(regex, self.word)
        if match is not None:
            return match.group().split()
        return match

    def get_ho_nam_onset(self): # ห นำ
        regex = r"ห[ก-ฮ]"
        match = re.search(regex, self.word)
        if match is not None:
            return match.group().split()
        return match

    def get_ao_yo_onset(self): # อย
        match = re.search('อย', self.word)
        if match is not None:
            return match.group().split()
        return match

    def find_first_consonant(self):
        if self.diphthong() is not None:
            return self.diphthong()
        elif self.consonants_before_H() is not None:
            return self.consonants_before_H()
        elif self.get_ao_yo_onset() is not None:
            return self.get_ao_yo_onset()
        else:
            # match = re.search(self.consonants_in_unicode, self.word)
            # return match.group()


    def get_initial(self, word):
        consonants_in_unicode = r"[ก-ร|ล|ว-ฮ]"

        if self.get_diphthong() is not None:
            character = self.get_diphthong()[0]
        elif self.get_ao_yo_onset() is not None:
            character = self.get_ao_yo_onset()[0]
        elif self.get_ho_nam_onset() is not None:
            character = self.get_ho_nam_onset()[0]
        else:
            match = re.search(consonants_in_unicode, self.word)
            if match is not None:
                character = match.group()

        # Check เสียงของพยัญชนะต้น
        if character in ['ก', 'ง', 'จ', 'ฉ', 'ซ', 'บ', 'ป', 'ผ', 'ฝ', 'ฟ', 'ม', 'ร', 'ว', 'ห', 'อ', 'ฮ']:
            phonetic = character
        elif character in ['ข', 'ฃ']:
            phonetic = 'ข'
        elif character in ['ค', 'ฅ', 'ฆ']:
            phonetic = 'ค'
        elif character in ['ช', 'ฌ']:
            phonetic = 'ช'
        elif character in ['ญ', 'ย']:
            phonetic = 'ย'
        elif character in ['ฎ', 'ด']:
            phonetic = 'ด'
        elif character in ['ฏ', 'ต']:
            phonetic = 'ต'
        elif character in ['ฑ', 'ฒ', 'ท', 'ธ']:
            phonetic = 'ท'
        elif character in ['ฐ', 'ถ']:
            phonetic = 'ถ'
        elif character in ['ณ', 'น']:
            phonetic = 'น'
        elif character in ['พ', 'ภ']:
            phonetic = 'พ'
        elif character in ['ล', 'ฬ']:
            phonetic = 'ล'
        elif character in ['ศ', 'ษ', 'ส']:
            phonetic = 'ส'

        # Check อักษรสูง กลาง ต่ำ
        if character in ['ก', 'จ', 'ฎ', 'ฏ', 'ด', 'ต', 'บ', 'ป', 'อ']:
            tone =
        elif character in ['ข', 'ฃ', 'ฉ', 'ฐ', 'ถ', 'ผ', 'ฝ', 'ศ', 'ษ', 'ส', 'ห']:
            tone =
        elif character in ['ค', 'ฅ', 'ฆ', 'ช', 'ซ', 'ฌ', 'ฑ', 'ฒ', 'ท', 'ธ', 'พ', 'ฟ', 'ภ', 'ฮ']:
            tone =
        elif character in ['ง', 'ญ', 'ณ', 'น', 'ม', 'ย', 'ร', 'ล', 'ว', 'ฬ']:
            tone =

        return Consonant(_format, phonetic, tone)

        # return 'ก'

    def get_medial(self, word):
        if self.get_diphthong() is not None:
            character = self.get_diphthong()[1]
        elif self.get_ao_yo_onset() is not None:
            character = self.get_ao_yo_onset()[1]
        elif self.get_ho_nam_onset() is not None:
            character = self.get_ho_nam_onset()[1]
        return None

    def get_nucleus(self, word):
        # สระเสียงสั้น หรือ รัสสระ (อ่านว่า รัด-สะ-สะ-หระ)
        ['อะ', 'อิ', 'อึ', 'อุ', 'เอะ', 'แอะ', 'โอะ', 'เอาะ', 'เออะ', 'เอียะ', 'เอือะ', 'อัวะ', 'ฤ', 'ฦ', 'อำ', 'ใอ', 'ไอ', 'เอา']
            return Vowel(vowel, 'short')
        # สระเสียงยาว หรือ ทีฆสระ (อ่านว่า ที-คะ-สะ-หระ)
        ['อา', 'อี', 'อือ', 'อู', 'เอ', 'แอ', 'โอ', 'ออ', 'เออ', 'เอีย', 'เอือ', 'อัว', 'ฤา', 'ฦา']
            return Vowel(vowel, 'long')

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

    def get_tone(self, word, ):
        tone_marks = ['\u0E48', '\u0E49', '\u0E4A', '\u0E4B'] # เอก โท ตรี จัตวา
        for index, tone_mark in enumerate(tone_marks, start=1):
            if re.search(tone_mark, self.word):
                return tone_mark
        return None

    def get_type(self, word):

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

        middle_character = ['ก', 'จ', 'ฎ', 'ฏ', 'ด', 'ต', 'บ', 'ป', 'อ']
        high_character = ['ข', 'ฃ', 'ฉ', 'ฐ', 'ถ', 'ผ', 'ฝ', 'ศ', 'ษ', 'ส', 'ห']
        pair_low_character = ['ค', 'ฅ', 'ฆ', 'ช', 'ซ', 'ฌ', 'ฑ', 'ฒ', 'ท', 'ธ', 'พ', 'ฟ', 'ภ', 'ฮ']
        single_low_character = ['ง', 'ญ', 'ณ', 'น', 'ม', 'ย', 'ร', 'ล', 'ว', 'ฬ']
        '''

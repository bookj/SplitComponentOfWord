from ..types import *
import re

from enum import Enum

class WordAnalyzer:
    def __init__(self):
        pass

    # def process(self, text):
    #     # เช็ค พยัญชนะ สระ ตัวสะกด
    #     # text = 'การบ้าน'
    #     pronunciations = []
    #     '''
    #     s1 = Syllable('การ',
    #             initial = self.get_initial('การ'),
    #             medial = None,
    #             nucleus = None,
    #             coda = None,
    #             tone = None,
    #             _type = None)
    #     s2 = Syllable()
    #     '''
    #     # check
    #     pronunciations.append(s1)
    #     pronunciations.append(s2)
    #
    #     # return Word(text, pronunciations)

    def get_ho_nam_onset(self, word): # ห นำ
        regex = r"ห[ก-ฮ]"
        match = re.search(regex, word)
        if match is not None:
            return match.group().split()
        return match

    def get_diphthong(self, word): # คำควบกล้ำ
        regex = r"[ก-ร|ล|ว-ฮ][ร|ล|ว]"
        match = re.search(regex, word)
        if match is not None:
            return match.group().split()
        return match

    def get_ao_yo_onset(self, word): # อย
        match = re.search('อย', word)
        if match is not None:
            return match.group().split()
        return match

    def get_initial(self, word):
        consonants_in_unicode = r"[ก-ร|ล|ว-ฮ]"

        if self.get_ao_yo_onset(word) is not None:
            _format = self.get_ao_yo_onset(word)[0]

        elif self.get_diphthong(word) is not None:
            _format = self.get_diphthong(word)[0]

        elif self.get_ho_nam_onset(word) is not None:
            _format = self.get_ho_nam_onset(word)[0]

        else:
            match = re.search(consonants_in_unicode, word)
            if match is not None:
                _format = match.group()

        # Check เสียงของพยัญชนะต้น
        if _format in ['ก', 'ง', 'จ', 'ฉ', 'ซ', 'บ', 'ป', 'ผ', 'ฝ', 'ฟ', 'ม', 'ร', 'ว', 'ห', 'อ', 'ฮ']:
            phonetic = _format
        elif _format in ['ข', 'ฃ']:
            phonetic = 'ข'
        elif _format in ['ค', 'ฅ', 'ฆ']:
            phonetic = 'ค'
        elif _format in ['ช', 'ฌ']:
            phonetic = 'ช'
        elif _format in ['ญ', 'ย']:
            phonetic = 'ย'
        elif _format in ['ฎ', 'ด']:
            phonetic = 'ด'
        elif _format in ['ฏ', 'ต']:
            phonetic = 'ต'
        elif _format in ['ฑ', 'ฒ', 'ท', 'ธ']:
            phonetic = 'ท'
        elif _format in ['ฐ', 'ถ']:
            phonetic = 'ถ'
        elif _format in ['ณ', 'น']:
            phonetic = 'น'
        elif _format in ['พ', 'ภ']:
            phonetic = 'พ'
        elif _format in ['ล', 'ฬ']:
            phonetic = 'ล'
        elif _format in ['ศ', 'ษ', 'ส']:
            phonetic = 'ส'

        # Check อักษรสูง กลาง ต่ำ
        consonants = { "middle" : ['ก', 'จ', 'ฎ', 'ฏ', 'ด', 'ต', 'บ', 'ป', 'อ'], \
        "high" : ['ข', 'ฃ', 'ฉ', 'ฐ', 'ถ', 'ผ', 'ฝ', 'ศ', 'ษ', 'ส', 'ห'], \
        "pair_low" : ['ค', 'ฅ', 'ฆ', 'ช', 'ซ', 'ฌ', 'ฑ', 'ฒ', 'ท', 'ธ', 'พ', 'ฟ', 'ภ', 'ฮ'], \
        "single_low" : ['ง', 'ญ', 'ณ', 'น', 'ม', 'ย', 'ร', 'ล', 'ว', 'ฬ']
        }
        for key, value in consonants.items():
            if _format in value:
                if key == "middle":
                    tone = ConsonantTone.middle
                elif key == "high":
                    tone = ConsonantTone.high
                elif key == "pair_low":
                    tone = ConsonantTone.pair_low
                elif key == "single_low":
                    tone = ConsonantTone.single_low
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

    def find_vowel(self):
        vowels = { \
        "เ" : ['เ[ก-ฮ]+ียะ', 'เ[ก-ฮ]+ือะ', 'เ[ก-ฮ]+ีย', 'เ[ก-ฮ]+ือ', \
                    'เ[ก-ฮ]+าะ', 'เ[ก-ฮ]+อะ' , 'เ[ก-ฮ]+อ' , 'เ[ก-ฮ]+า', \
                    'เ[ก-ฮ]+ะ', 'เ[ก-ฮ]+'], # สระที่ขึ้นต้นด้วยตัว เอ
        "แ" : ['แ[ก-ฮ]+ะ', 'แ[ก-ฮ]+'], # สระที่ขึ้นต้นด้วยตัว แอ
        "โ" : ['โ[ก-ฮ]+ะ', 'โ[ก-ฮ]+'], # สระที่ขึ้นต้นด้วยตัว โอ
        "\u0E" : ['[ก-ฮ]+ัวะ', '[ก-ฮ]+ัว', '[ก-ฮ]+ั'] # สระที่ขึ้นต้นด้วยตัว อัว
        }
        vowels_in_unicode = r"[\u0E30-\u0E39|\u0E40-\u0E45]"
        match = re.search(vowels_in_unicode, self.word)
        if match is not None:
            if self.find_tone_mark() is not None:
                del_tone_mark = self.word.replace(self.find_tone_mark(), '')
            else:
                del_tone_mark = self.word

            if match.group() == 'เ':
                for vowel in self.vowels_before_A :
                    if re.search(vowel, del_tone_mark):
                        return vowel.replace('[ก-ฮ]+', 'อ')
            elif match.group() == 'แ':
                for vowel in self.vowelsBeforeAe :
                    if re.search(vowel, del_tone_mark):
                        return vowel.replace('[ก-ฮ]+', 'อ')
            elif match.group() == 'โ':
                for vowel in self.vowels_before_O:
                    if re.search(vowel, del_tone_mark):
                        return vowel.replace('[ก-ฮ]+', 'อ')
            elif match.group() == 'ั':
                for vowel in self.vowels_before_Ua:
                    if re.search(vowel, del_tone_mark):
                        return vowel.replace('[ก-ฮ]+', 'อ')
            elif match.group() == 'ใ' or match.group() == 'ไ' :
                return match.group() + 'อ'
            else:
                return 'อ' + match.group()
        else:
            return None

    def get_nucleus(self, word):
        vowels = { \
        # สระเสียงสั้น หรือ รัสสระ (อ่านว่า รัด-สะ-สะ-หระ)
        # สระเสียงยาว หรือ ทีฆสระ (อ่านว่า ที-คะ-สะ-หระ)
        "short" : ['อะ', 'อิ', 'อึ', 'อุ', 'เอะ', 'แอะ', 'โอะ', 'เอาะ', 'เออะ', 'เอียะ', 'เอือะ', 'อัวะ', 'ฤ', 'ฦ', 'อำ', 'ใอ', 'ไอ', 'เอา'], \
        "long" : ['อา', 'อี', 'อือ', 'อู', 'เอ', 'แอ', 'โอ', 'ออ', 'เออ', 'เอีย', 'เอือ', 'อัว', 'ฤา', 'ฦา']
        }
        for key, value in vowels.items():
            if self.find_vowel() in value:
                return Vowel(self.find_vowel(), key)

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

    # def get_type(self, word):

# if __name__ == '__main__':
    # input_data = input("Enter your expression: ")
print(WordAnalyzer().get_initial('กาว'))

        # # มาตราตัวสะกด
        # kk = ['ก', 'ข', 'ค', 'ฆ']
        # kd = ['จ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'ฎ', 'ฏ', 'ฑ', 'ฒ', 'ช', 'ซ', 'ศ', 'ษ', 'ส']
        # kb = ['บ', 'ป', 'พ', 'ภ', 'ฟ']
        # kng = ['ง']
        # kn = ['น', 'ณ', 'ญ', 'ร', 'ล', 'ฬ']
        # km - ['ม']
        # ky = ['ย']
        # kw = ['ว']

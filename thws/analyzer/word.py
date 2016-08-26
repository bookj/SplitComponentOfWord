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
        return Consonant(_format, phonetic, tone) # return 'ก'

    def get_medial(self, word):
        if self.get_diphthong() is not None:
            character = self.get_diphthong()[1]
        elif self.get_ao_yo_onset() is not None:
            character = self.get_ao_yo_onset()[1]
        elif self.get_ho_nam_onset() is not None:
            character = self.get_ho_nam_onset()[1]
        return None

    def find_vowel(self, word):
        vowels = { \
        "เ" : ['เ[ก-ฮ]+ียะ', 'เ[ก-ฮ]+ือะ', 'เ[ก-ฮ]+ีย', 'เ[ก-ฮ]+ือ', \
                    'เ[ก-ฮ]+าะ', 'เ[ก-ฮ]+อะ' , 'เ[ก-ฮ]+อ' , 'เ[ก-ฮ]+า', \
                    'เ[ก-ฮ]+ะ', 'เ[ก-ฮ]+'], # สระที่ขึ้นต้นด้วยตัว เอ
        "แ" : ['แ[ก-ฮ]+ะ', 'แ[ก-ฮ]+'], # สระที่ขึ้นต้นด้วยตัว แอ
        "โ" : ['โ[ก-ฮ]+ะ', 'โ[ก-ฮ]+'], # สระที่ขึ้นต้นด้วยตัว โอ
        "\u0E31" : ['[ก-ฮ]+ัวะ', '[ก-ฮ]+ัว', '[ก-ฮ]+ั'] # สระที่ขึ้นต้นด้วยตัว อัว
        }
        vowels_in_unicode = r"[\u0E30-\u0E39|\u0E40-\u0E45]"
        match = re.search(vowels_in_unicode, word)
        if match is not None:
            if self.get_tone(word) is not None:
                del_tone_mark = word.replace(self.get_tone(word), '')
            else:
                del_tone_mark = word

            if match.group() == 'ใ' or match.group() == 'ไ' :
                return match.group() + 'อ'

            for key, value in vowels.items():
                if match.group() == key:
                    for vowel in value:
                        if re.search(vowel, del_tone_mark):
                            return vowel.replace('[ก-ฮ]+', 'อ')
            return 'อ' + match.group()
        return None

    def get_nucleus(self, word):
        # สระเสียงสั้น หรือ รัสสระ (อ่านว่า รัด-สะ-สะ-หระ)
        # สระเสียงยาว หรือ ทีฆสระ (อ่านว่า ที-คะ-สะ-หระ)
        vowels = { \
        "short" : ['อะ', 'อิ', 'อึ', 'อุ', 'เอะ', 'แอะ', 'โอะ', 'เอาะ', 'เออะ', 'เอียะ', 'เอือะ', 'อัวะ', 'ฤ', 'ฦ', 'อำ', 'ใอ', 'ไอ', 'เอา'], \
        "long" : ['อา', 'อี', 'อือ', 'อู', 'เอ', 'แอ', 'โอ', 'ออ', 'เออ', 'เอีย', 'เอือ', 'อัว', 'ฤา', 'ฦา']
        }
        for key, value in vowels.items():
            if self.find_vowel(word) in value:
                return Vowel(self.find_vowel(word), key)

    def find_final_consonant(self, word): # spelling
        if self.get_tone(word) is not None:
            del_tone_mark = re.sub(self.get_tone(word), '', word)
        else:
            del_tone_mark = word
        _initial = self.get_initial(del_tone_mark)
        del_first_consonant = re.sub(_initial.format, '', del_tone_mark)
        # ลบ อ ออกจากสระ เช่น แอะ ==> แ-ะ
        vowel_del_OO = re.sub('อ', '', self.find_vowel(word))
        final_consonant = re.sub(vowel_del_OO, '', del_first_consonant)
        if final_consonant == '' :
            return None
        return final_consonant

    # def get_coda(self, character):
    def get_coda(self, word):
        # มาตราตัวสะกด
        codas = { \
        'ก' : ['ก', 'ข', 'ค', 'ฆ'], \
        'ด' : ['จ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'ฎ', 'ฏ', 'ฑ', 'ฒ', 'ช', 'ซ', 'ศ', 'ษ', 'ส'], \
        'บ' : ['บ', 'ป', 'พ', 'ภ', 'ฟ'], \
        'ง' : ['ง'], \
        'น' : ['น', 'ณ', 'ญ', 'ร', 'ล', 'ฬ'], \
        'ม' : ['ม'], \
        'ย' : ['ย'], \
        'ว' : ['ว']
        }
        character = self.find_final_consonant(word)
        if character is not None:
            for key, value in codas.items():
                if character in value:
                    return Consonant(character, key)

    def get_tone(self, word):
        tone_marks = ['\u0E48', '\u0E49', '\u0E4A', '\u0E4B'] # [รูป] เอก โท ตรี จัตวา
        for index, tone_mark in enumerate(tone_marks, start=1):
            if re.search(tone_mark, word):
                return tone_mark
        return None

    # def get_type(self, word):
        # คำเป็น
        #     คำประสมด้วยสระเสียงยาว ในแม่ ก กา รวมทั้งสระเสียงสั้น อำ ใอ ไอ เอา
        #     เป็นคำที่มีตัวสะกดอยู่ในแม่กง กน กม เกย เกอว เช่น จง มั่น ชม เชย ดาวไพเป็น
        # คำตาย
        #     เป็นคำที่ผสมด้วยสระเสียงสั้นในแม่ ก กา เช่น จะ ปะ ทุ
        #     เป็นคำที่มีตัวสะกดในแม่ กก กด กบ เช่น นัด พบ นก กระผม

# if __name__ == '__main__':
    # input_data = input("Enter your expression: ")

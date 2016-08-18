import re

class split_component_of_word:
    def __init__(self, word):
        self.word = word
        self.
        self.vowels_before_A = ['เ[ก-ฮ]+ียะ', 'เ[ก-ฮ]+ือะ', 'เ[ก-ฮ]+ีย', 'เ[ก-ฮ]+ือ', \
                                'เ[ก-ฮ]+าะ', 'เ[ก-ฮ]+อะ' , 'เ[ก-ฮ]+อ' , 'เ[ก-ฮ]+า', \
                                'เ[ก-ฮ]+ะ', 'เ[ก-ฮ]+'] # สระที่ขึ้นต้นด้วยตัว เอ
        self.vowels_before_Ae = ['แ[ก-ฮ]+ะ', 'แ[ก-ฮ]+'] # สระที่ขึ้นต้นด้วยตัว แอ
        self.vowels_before_O = ['โ[ก-ฮ]+ะ', 'โ[ก-ฮ]+'] # สระที่ขึ้นต้นด้วยตัว โอ
        self.vowels_before_Ua = ['[ก-ฮ]+ัวะ', '[ก-ฮ]+ัว', '[ก-ฮ]+ั'] # สระที่ขึ้นต้นด้วยตัว อัว

    def find_tone_mark(self):
        tone_marks = ['\u0E48', '\u0E49', '\u0E4A', '\u0E4B'] # เอก โท ตรี จัตวา
        for tone_mark in tone_marks:
            if re.search(tone_mark, self.word):
                return tone_mark
        return None

    def diphthong(self): # คำควบกล้ำ
        regex = r"[^ห|ก-ร|ล|ว-ฮ][ร|ล|ว]"
        match = re.search(regex, self.word)
        if match is not None:
            return match.group()
        return match

    def consonants_before_H(self): # ห นำ
        regex = r"ห[ก-ฮ]"
        match = re.search(regex, self.word)
        if match is not None:
            return match.group()
        return match

    def consonants_before_OY(self): # อย
        match = re.search('อย', self.word)
        if match is not None:
            return match.group()
        return match

    def find_first_consonant(self):
        if self.diphthong() is not None:
            return self.diphthong()
        elif self.consonants_before_H() is not None:
            return self.consonants_before_H()
        elif self.consonants_before_OY() is not None:
            return self.consonants_before_OY()
        else:
            # match = re.search(self.consonants_in_unicode, self.word)
            # return match.group()

    def find_vowel(self):
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

    def findFinalConsonant(self): # spelling
        if self.find_tone_mark(self.word) is not None:
            deltone_mark = re.sub(find_tone_mark(self.word), '', self.word)
        else:
            deltone_mark = self.word
        delFirstConsonant = re.sub(find_first_consonant(deltone_mark), '', deltone_mark)
        finalConsonant = re.sub(find_vowel(self.word), '', delFirstConsonant)
        if finalConsonant == '' :
            return None
        return finalConsonant

'''
word = input("ป้อนคำ 1 คำ : ")
print(find_first_consonant(word))
print(find_vowel(word))
print(findFinalConsonant(word))
print(find_tone_mark(word))
'''

'''
if __name__ == '__main__':
    input_data = input("Enter your expression: ")
    print(Calculator(input_data).calculate())
'''

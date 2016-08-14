import re
'''
middleChar = ['ก', 'จ', 'ฎ', 'ฏ', 'ด', 'ต', 'บ', 'ป', 'อ']
highChar = ['ข', 'ฃ', 'ฉ', 'ฐ', 'ถ', 'ผ', 'ฝ', 'ศ', 'ษ', 'ส', 'ห']
'''
class SplitComponentOfWord:
    def __init__(self, word):
        self.word = word
        self.vowelsInUnicode = r"[\u0E30-\u0E39|\u0E40-\u0E45]"
        self.consonantsInUnicode = r"[ก-ร|ล|ว-ฮ]+"
        self.toneMarks = ['่', '้', '๊', '๋']
        self.vowelsBeforeA = ['เ[ก-ฮ]+ียะ', 'เ[ก-ฮ]+ือะ', 'เ[ก-ฮ]+ีย', 'เ[ก-ฮ]+ือ', \
                         'เ[ก-ฮ]+าะ', 'เ[ก-ฮ]+อะ' , 'เ[ก-ฮ]+อ' , 'เ[ก-ฮ]+า', \
                         'เ[ก-ฮ]+ะ', 'เ[ก-ฮ]+'] # สระที่ขึ้นต้นด้วยตัว เ-
        self.vowelsBeforeAe = ['แ[ก-ฮ]+ะ', 'แ[ก-ฮ]+'] # สระที่ขึ้นต้นด้วยตัว แ-
        self.vowelsBeforeO = ['โ[ก-ฮ]+ะ', 'โ[ก-ฮ]+'] # สระที่ขึ้นต้นด้วยตัว โ-
        self.vowelsBeforeUa = ['[ก-ฮ]+ัวะ', '[ก-ฮ]+ัว', '[ก-ฮ]+ั'] # สระที่ขึ้นต้นด้วยตัว -ัว


    def findToneMark(self):
        for toneMark in self.toneMarks:
            if re.search(toneMark, self.word):
                return toneMark
        return None

    def diphthong(self):
        regex = r"[^ห|ก-ร|ล|ว-ฮ][ร|ล|ว]"
        match = re.search(regex, self.word)
        if match is not None:
            return match.group()
        return match

    def consonantsBeforeH(self): # ห นำ
        regex = r"ห[ก-ฮ]"
        match = re.search(regex, self.word)
        if match is not None:
            return match.group()
        return match

    def consonantsBeforeOY(self): # อย
        match = re.search('อย', self.word)
        if match is not None:
            return match.group()
        return match

    def findFirstConsonant(self):
        if self.diphthong() is not None:
            return self.diphthong()
        elif self.consonantsBeforeH() is not None:
            return self.consonantsBeforeH()
        elif self.consonantsBeforeOY() is not None:
            return self.consonantsBeforeOY()
        else:
            match = re.search(self.consonantsInUnicode, self.word)
            return match.group()

    def findVowel(self):
        match = re.search(vowelsInUnicode, self.word)
        if match is not None:
            if match.group() == 'เ':
                for vowel in self.vowelsBeforeA :
                    if re.search(vowel, self.word):
                        return vowel.replace('[ก-ฮ]+', '')
            elif match.group() == 'แ':
                for vowel in self.vowelsBeforeAe :
                    if re.search(vowel, self.word):
                        return vowel.replace('[ก-ฮ]+', '')
            elif match.group() == 'โ':
                for vowel in self.vowelsBeforeO:
                    if re.search(vowel, self.word):
                        return vowel.replace('[ก-ฮ]+', '')
            elif match.group() == 'ั':
                for vowel in self.vowelsBeforeUa:
                    if re.search(vowel, self.word):
                        return vowel.replace('[ก-ฮ]+', '')
            else:
                return match.group()
        else:
            return None

    def findFinalConsonant(self): # spelling
        if findToneMark(self.word) is not None:
            delToneMark = re.sub(findToneMark(self.word), '', self.word)
        else:
            delToneMark = self.word
        delFirstConsonant = re.sub(findFirstConsonant(delToneMark), '', delToneMark)
        finalConsonant = re.sub(findVowel(self.word), '', delFirstConsonant)
        if finalConsonant == '' :
            return None
        return finalConsonant

'''
word = input("ป้อนคำ 1 คำ : ")
print(findFirstConsonant(word))
print(findVowel(word))
print(findFinalConsonant(word))
print(findToneMark(word))
'''

'''
if __name__ == '__main__':
    input_data = input("Enter your expression: ")
    print(Calculator(input_data).calculate())
'''

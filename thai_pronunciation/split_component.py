class split_component_of_word:
    def __init__(self, word):

    def find_tone_mark(self):
        tone_marks = ['\u0E48', '\u0E49', '\u0E4A', '\u0E4B'] # เอก โท ตรี จัตวา
        for tone_mark in tone_marks:
            if re.search(tone_mark, self.word):
                return tone_mark
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
if __name__ == '__main__':
    input_data = input("Enter your expression: ")
    print(Calculator(input_data).calculate())
'''

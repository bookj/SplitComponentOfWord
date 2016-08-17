from ..types import Consonant, Syllable

class WordAnalyzer:
    def __init__(self):
        kk = [ก ข ค ฆ]
        kd = [จ ด ต ถ ท ธ ฎ ฏ ฑ ฒ ช ซ ศ ษ ส]
        kb = [บ ป พ ภ ฟ]
        pass
    def process(self, text):
        # เช็ค พยัญชนะ สระ ตัวสะกด
        text = 'การบ้าน'
        pronunciations = []

        s1 = Syllable('การ',
                initial=self.get_initial('การ'))
        s2 = Syllable()
        # check
        pronunciations.append(s1)
        pronunciations.append(s2)

        return Word(text, pronunciations)

    def get_coda(self, character):
        if character in [ก ข ค ฆ]:
            return Consonant(character, 'ก')

    def get_initial(self, word):
        return 'ก'

from enum import Enum
class SyllableTone(Enum):
    ordinary = 0    # สามัญ
    first = 1       # เอก
    second = 2      # โท
    third = 3       # ตรี
    fourth = 4      # จัตวา

class Consonant:
    def __init__(self, _format = None, phonetic = None, tone = None):
        self.format = _format # 'ฆ'
        self.phonetic = phonetic # 'ค'
        self.tone = tone

class Vowel:
    def __init__(self):
        self.format = '' # 'อะ' 'อา'
        self.type = '' # short, long


class Syllable:
    def __init__(self,
            _format = None,
            initial = None,
            medial = None,
            nucleus = None,
            coda = None,
            tone = None,
            _type = None):
        '''
            สามัญ => ordinary => 0
        '''
        self.format = _format # 'การ'
        self.initial = initial # 'ก'
        self.medial = medial # None
        self.nucleus = nucleus # 'อา'
        self.coda = coda # 'ร'
        self.tone = tone # SyllableTone.ordinary # สามัญ
        self.type = _type # คำเป็น คำตาย

    @property
    def onset(self):
        return [self.initial, self.medial]

    @property
    def rime(self):
        return [self.nucleus, self.coda]

class Word:
    def __init__(self, _fomat = None, pronunciations = []):
        self.format = _format # 'การ'
        self.pronunciations = pronunciations # list of Syllable

    def count_syllable(self):
        return len(self.pronunciations)

class Meter:
    def __init__(self):
        # วรรค
        self.format = '' # 'ถึงม้วยดินสิ้นฟ้ามหาสมุทร'
        self.words = []

    def count(self):
        return len(self.words)

    def count_syllable(self):
        return sum([word.count_syllable() for word in self.words])

class Chapter:
    self __init__(self, meters=[]):
        self.meters = meters #

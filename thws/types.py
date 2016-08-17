from enum import Enum
class SyllableTone(Enum):
    ordinary = 0    # สามัญ
    first = 1       # เอก
    second = 2      # โท
    third = 3       # ตรี
    fourth = 4      # จัตวา

class Consonant:
    def __init__(self):
        Kk = [ก ข ค ฆ]
        Kd = [จ ด ต ถ ท ธ ฎ ฏ ฑ ฒ ช ซ ศ ษ ส]
        Kb = [บ ป พ ภ ฟ]
        Kng = []
        Kn = []
        Km

        self.format = '' # 'ฆ'
        self.phonetic = '' # 'ค'
        self.tone = ''

class Vowel:
    def __init__(self):
        self.format = '' # 'อะ' 'อา'
        self.type = '' # short, long


class Syllable:
    def __init__(self):
        '''
            สามัญ => ordinary => 0
        '''
        self.format = '' # 'การ'
        self.initial = '' # 'ก'
        self.medial = '' # None
        self.nucleus = '' # 'อา'
        self.coda = '' # 'ร'
        self.tone = SyllableTone.ordinary # สามัญ
        self.type = '' # คำเป็น คำตาย

    @property
    def onset(self):
        return [self.initial, self.medial]

    @property
    def rime(self):
        return [self.nucleus, self.coda]

class Word:
    def __init__(self):
        self.format = '' # 'การ'
        self.pronunciation = [] # list of Syllable

class Meter:
    def __init__(self):
        # วรรค
        self.format = '' # 'ถึงม้วยดินสิ้นฟ้ามหาสมุทร'
        self.words = []

class Chapter:
    self __init__(self, meters=[]):
        self.meters = meters #

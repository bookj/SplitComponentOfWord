#!/usr/bin/python
#im ..types import Chapter

#import MeterAnalyzer

class ChapterAnalyzer():
    def __init__(self):
        pass

    def process(self, chapter_texts):
        #meter = MeterAnalyzer()
        current_position = 0
        last_position = 0
        poems = []
        interval = []
        while(True):            #Split poem
            current_position = chapter_texts.find(' ', last_position+1)
            if current_position == -1:
                break
            poems.append(chapter_texts[last_position : current_position])
            last_position = current_position

        for chapter in poems:           #split each poem & add in list
            print(chapter)
            #interval.append(meter.processe(chapter))
        '''
        for word in interval:
            print (word)

        print (poems)
        return Chapter()
        '''

if True:
    chapter = ChapterAnalyzer()
    chapter.process("ถึงม้วยดินสิ้นฟ้ามหาสมุทร ไม่สิ้นสุดความรักสมัครสมาน ")

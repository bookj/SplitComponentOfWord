#!/usr/bin/python
import PyICU
import re

class MeterAnalyzer:
    def __init__(self):
        #non_thai_char = [^ก-ฮ | '/u0E2F'-'/u0E3A' | '/u0E40'-'/u0E5B'
        pass
    def process(self, text):
        print("Text :" + text)
        boundary = PyICU.BreakIterator.createWordInstance(PyICU.Locale("th"))
        boundary.setText(text)
        last_position = boundary.first()
        words = []
        try:
            while(True):
                current_position = next(boundary)
                '''
                if True:
                    print("Current Position : " + str(current_position))
                    print("Last Position : " + str(last_position))
                '''
                thai_word = text[last_position : current_position]
                #if re.match(thai_word
                words.append(thai_word)
                last_position = current_position
        except StopIteration:
            pass

        return words


if True:
    meter = MeterAnalyzer()
    print(meter.process(r"ถึงม้วยดิน 'สิ้น'ฟ้า มหา?สมุทร?"))
    [^ก-ฮ'/u0E2F'-'/u0E3A''/u0E40'-'/u0E5B']



#print(splitword("สวัสดีครับผมชื่อมิ้นท์ครับยินดีที่ได้รู้จักครับผม"))
#print(splitword("ถึงม้วยดินสิ้นฟ้ามหาสมุทร ไม่สิ้นสุดความรักสมัครสมาน แม้เกิดในใต้ฟ้าสุธาธาร ขอพบพานพิศวาสไม่คลาดคลา แม้เนื้อเย็นเป็นห้วงมหรรณพ พี่ขอพบศรีสวัสดิ์เป็นมัจฉา แม่เป็นบัวตัวพี่เป็นภุมรา เชยผกาโกสุมประทุมทอง"))

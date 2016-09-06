#!/usr/bin/python
import PyICU
import re

class MeterAnalyzer:
    def __init__(self):
        self.words = []
        self.special_character = r"[^ก-ฮ\u0E2F-\u0E3A\u0E40-\u0E5B]"

    def process(self, text):
        words = strip_special_character(text)
        self.words = self.separate_word(words)
        return self.words

    def strip_special_character(self, words):
        new_words = ''
        new_words_list = re.split(self.special_character, words)
        for word in new_words_list:
            if word != '':
                new_words = new_words + word
        return new_words

    def separate_word(self, text):
        boundary = PyICU.BreakIterator.createWordInstance(PyICU.Locale("th"))
        boundary.setText(text)
        last_position = boundary.first()
        words = []
        try:
            while(True):
                current_position = next(boundary)
                words.append(text[last_position : current_position])
                last_position = current_position
        except StopIteration:
            pass

        return words

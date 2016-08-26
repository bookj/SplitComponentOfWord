#!/usr/bin/python
import PyICU
import re

class MeterAnalyzer:
    def __init__(self):
        self.words = []
        self.special_character = r"[^ก-ฮ\u0E2F-\u0E3A\u0E40-\u0E5B]"

    def process(self, text):
        words = self.separate_word(text)
        self.words = strip_special_character(words)
        return self.words

    def strip_special_character(self, words):
        new_words = []
        for word in words:
            if not re.search(self.special_character, word):
                new_words.append(word)
            else if:
                
        return new_words

    def separate_word(self, word):
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

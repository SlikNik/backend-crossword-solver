#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Nikal Morgan"

import re


def find_possible_words(test_word, words):
    pattern = r'[a-z]'
    replace = test_word.replace(' ', pattern)

    for word in words:
        if re.search(replace, word):
            if len(test_word) == len(word):
                print(word)


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    print('Please enter a word to solve.')
    test_word = input('Use spaces to signify unknown letters: ').lower()
    if test_word == '':
        raise NotImplementedError('Please complete this')
    find_possible_words(test_word, words)


if __name__ == '__main__':
    main()

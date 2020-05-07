import regex
import re
from collections import Counter

text = open('Alice29.txt', 'r').read()
words = re.findall(r'\w+', text.lower())
word_count = Counter(words)

def make_word_string(input_string):
    word_string = ''
    for word in input_string:
        word_string = word_string + word
    return word_string

def print_dict():
    for key in word_count: print(key, word_count[key])
    return

print(len(make_word_string(words)))







"""
Name generator

Using Kevin's name generator because mine isn't available in China
"""

import random
import string

vowels = ['a', 'e', 'i', 'o', 'u']
consonants = list(set(string.ascii_lowercase).difference(vowels))

patterns = ["VCCVVC", "CVCVCC", "VCVCVC", "CVCCVC", "CVVCCVVC", "CVCVC",
        "CCVCVC-CVCVCC", "VVCV", "VCVCVVCV", "CVCV", "CVCVC"]

def replace_char(c):
    if c == 'V':
        return random.choice(vowels)
    elif c == '-':
        return '-'
    else:
        return random.choice(consonants)

def replace(pattern):
    return "".join(list(map(replace_char, pattern)))

def randomName():
    return str.capitalize(replace(random.choice(patterns)))

def main():
    print(randomName())

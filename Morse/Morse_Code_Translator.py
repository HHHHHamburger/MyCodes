#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
'''
Created on 2017年3月14日
content >= u'\u4e00' and content <= u'\u9fff':
    reply = u'摩斯密码只支持英文和数字'
@author: HGladiator
'''
# DAH should be three DOTs.
# Space between DOTs and DAHs should be one DOT.
# Space between two letters should be one DAH.
# Space between two words should be DOT DAH DAH.

class morse(object):
    
    def __init__(self):
        super(morse, self).__init__()
        
    morseAlphabet = {
        'A': '.-',              'a': '.-',
        'B': '-...',            'b': '-...',
        'C': '-.-.',            'c': '-.-.',
        'D': '-..',             'd': '-..',
        'E': '.',               'e': '.',
        'F': '..-.',            'f': '..-.',
        'G': '--.',             'g': '--.',
        'H': '....',            'h': '....',
        'I': '..',              'i': '..',
        'J': '.---',            'j': '.---',
        'K': '-.-',             'k': '-.-',
        'L': '.-..',            'l': '.-..',
        'M': '--',              'm': '--',
        'N': '-.',              'n': '-.',
        'O': '---',             'o': '---',
        'P': '.--.',            'p': '.--.',
        'Q': '--.-',            'q': '--.-',
        'R': '.-.',             'r': '.-.',
        'S': '...',             's': '...',
        'T': '-',               't': '-',
        'U': '..-',             'u': '..-',
        'V': '...-',            'v': '...-',
        'W': '.--',             'w': '.--',
        'X': '-..-',            'x': '-..-',
        'Y': '-.--',            'y': '-.--',
        'Z': '--..',            'z': '--..',
        '0': '-----',           ',': '--..--',
        '1': '.----',           '.': '.-.-.-',
        '2': '..---',           '?': '..--..',
        '3': '...--',           ';': '-.-.-.',
        '4': '....-',           ':': '---...',
        '5': '.....',           "'": '.----.',
        '6': '-....',           '-': '-....-',
        '7': '--...',           '/': '-..-.',
        '8': '---..',           '(': '-.--.-',
        '9': '----.',           ')': '-.--.-',
        ' ': ' ',               '_': '..--.-',
        " " : "/",               '':'',      
}
    inverseMorseAlphabet = dict((v,k) for (k,v) in morseAlphabet.items())
    
    def decode(self,words):   #, positionInString = 0
        # parse a morse code string positionInString is the starting point for decoding
        '''
        if positionInString < len(words):
            morseLetter = ""
            for key,char in enumerate(words[positionInString:]):
                if char == " ":
                    positionInString = key + positionInString + 1
                    letter = self.inverseMorseAlphabet[morseLetter]
                    return letter + self.decode(words, positionInString)
                else:
                    morseLetter += char
        else:
            return ""
        '''
        word_list = words.split(' ')
        #print word_list
        letter = ''
        for word in word_list:
            letter += self.inverseMorseAlphabet[word]
        return letter

    def encode(self,words):
        code = ''
        for word in words:
            code += self.morseAlphabet[word]
            code += ' '
        return code


if __name__ == '__main__':
    testCode = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.-- "
    res = morse()
    print res.decode(testCode)
#     while (True):
#         words = raw_input('MESSAGE: ')
#         print 'your words is : %s' % words
#         flag = raw_input('decode<D> or encode<E>:')
#         if flag == 'D' or flag == 'd':
#             print 'your decoded words is : '
#             print res.decode(words)
#         elif flag == 'E' or flag == 'e':
#             print 'your encoded words is : '
#             print res.encode(words)
#         else :
#             print ' input error,please input again!'

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:46:16 2024

@author: surrealpartisan
"""

from random import random, randrange
import sys
import os.path
import codecs

def listify(filename, encoding='utf-8'):
    l = []
    with open(filename, encoding=encoding) as f:
        for line in f:
            if line[-1] == '\n':
                l.append(list(line[:-1]))
            else:
                l.append(list(line))
        maxlen = max([len(s) for s in l])
        for s in l:
            if len(s) < maxlen:
                s += [' ']*(maxlen-len(s))
    return l

def turn(originaldirection, turning):
    if originaldirection == '>':
        if turning:
            return 'V'
        else:
            return 'Ʌ'
    if originaldirection == '<':
        if turning:
            return 'Ʌ'
        else:
            return 'V'
    if originaldirection == 'V':
        if turning:
            return '<'
        else:
            return '>'
    if originaldirection == 'Ʌ':
        if turning:
            return '>'
        else:
            return '<'

def run(code):
    x = y = 0
    x_max = len(code[0])
    y_max = len(code)
    data = [False]
    datapointer = 0
    direction = '>'
    samedirectioncounter = 0
    cont = True
    while cont:
        command = sum([ord(symbol) for row in code[:y+1] for symbol in row[:x+1]]) % 1114112
        if command == 115:
            cont = False
        elif command == 187:
            datapointer += 1
            if datapointer > len(data) - 1:
                data += [False]
        elif command == 10229:
            if datapointer > 0:
                datapointer -= 1
            else:
                data = [False] + data
        elif command == 8635:
            data[datapointer] = not data[datapointer]
        elif command == 9997:
            datapointer2 = datapointer
            accumulator = 0
            while datapointer2 < len(data) and data[datapointer2]:
                accumulator += 1
                datapointer2 += 1
            print(chr(accumulator), end='')
        elif command == 191:
            userinput = input('>')
            data[datapointer] = bool(userinput)
        elif command == 1071:
            data[datapointer] = bool(randrange(2))
        elif command == 1509:
            direction = turn(direction, data[datapointer])

        if command != 1509:
            newdirection = ['>', '<', 'V', 'Ʌ', '>', '<', 'V'][(sum([ord(symbol) for row in code[:y+1] for symbol in row[:x+1]]) + x + y) % 7]
            if newdirection != direction:
                samedirectioncounter = 0
                direction = newdirection
            else:
                samedirectioncounter += 1

        if direction == '>':
            x = (x + 1) % x_max
        if direction == '<':
            x = (x - 1) % x_max
        if direction == 'V':
            y = (y + 1) % y_max
        if direction == 'Ʌ':
            y = (y - 1) % y_max

        if random() < 0.0005 + min(0.0005*samedirectioncounter, 0.5):
            datapointer2 = randrange(len(data))
            data[datapointer2] = not data[datapointer2]
    print('')

def run_from_file(filename, encoding='utf-8'):
    run(listify(filename, encoding=encoding))

if __name__ == '__main__':
    if len(sys.argv) < 2 or not os.path.exists(sys.argv[1]):
        print('Invalid file or no file given!')
        print('Usage: python Furchtbar.py <filename_or_path> <encoding_(optional)>')
        sys.exit(1)

    if len(sys.argv) > 2:
        encoding = sys.argv[2]
        try:
            codecs.lookup(sys.argv[2])
        except LookupError:
            print('Invalid encoding!')
            print('Usage: python Furchtbar.py <filename_or_path> <encoding_(optional)>')
            sys.exit(1)
    else:
        encoding = 'utf-8'

    try:
        run_from_file(sys.argv[1], encoding=encoding)
        sys.exit(0)
    except KeyboardInterrupt:
        print('\nKeyboard interrupt')
        sys.exit(0)
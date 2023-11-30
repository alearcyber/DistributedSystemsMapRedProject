#!/usr/bin/python3
import sys

def read_input(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def reducer2():
    word = None
    sentiment = 0
    data = read_input(sys.stdin)
    for w, s in data: #word and sentiment

        if word is None: #starting with nothing
            word = w
            sentiment += int(s)

        elif w == word: # continue counting current key
            sentiment += int(s)

        else: #found a new key. print and reset
            print(f"{word}\t{sentiment}")
            word = w
            sentiment = 0
            sentiment += int(s)
    #take care of last key
    if word is not None:
        print(f"{word}\t{sentiment}")

reducer2()

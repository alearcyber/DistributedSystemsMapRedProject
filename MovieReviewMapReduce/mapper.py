#!/usr/bin/python3
import sys

def read_input(stream):
    for line in stream:
        # split the line into words
        yield line.split()

def mapper(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    sentiment = dict()
    for tokens in data:
        for word in tokens[1:]:
            #skip words less than 4
            if len(word) <= 4 or ('NEG' in word) or ('POS' in word):
                continue

            #process word
            if word not in sentiment.keys():
                sentiment[word] = 0
            if tokens[0] == 'POS': #positive review
                sentiment[word] += 1
            else: #negative review
                sentiment[word] -= 1

    for word in sentiment.keys():
        print(f"{word}{separator}{sentiment[word]}")

mapper()

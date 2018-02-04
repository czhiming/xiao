#-*- coding:utf8 -*-
'''
Created on 17-10-20

@author: czm
'''
import sys
from collections import Counter
import json


filename = sys.argv[1]

def get_bigram(file_name):
    ss = []
    with open(file_name) as fp:
        for lines in fp:
            lines = lines.strip().split()
            bigram_ = []
            for i in range(len(lines)-1):
                bigram_.append(' '.join(lines[i:i+2]))
            ss += bigram_
    return ss

def get_trigram(file_name):
    ss = []
    with open(file_name) as fp:
        for lines in fp:
            lines = lines.strip().split()
            trigram_ = []
            for i in range(len(lines)-2):
                trigram_.append(' '.join(lines[i:i+3]))
            ss += trigram_
    return ss


def bigram(ss):
    counter = Counter(ss)
    bb = {}
    for word,freq in counter.most_common():
        bb[word] = freq
    with open(filename+'.bigram','w') as fp:
        json.dump(bb, fp, indent=2)

def trigram(ss):
    counter = Counter(ss)
    tt = {}
    for word, freq in counter.most_common():
        tt[word] = freq
    with open(filename + '.trigram', 'w') as fp:
        json.dump(tt, fp, indent=2)





if __name__ == '__main__':
    print 'Get bigram file...'
    bigram(get_bigram(filename))
    print 'Get trigram file...'
    trigram(get_trigram(filename))








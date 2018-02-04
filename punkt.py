#coding:utf-8

import sys
import nltk.data
import codecs

file_name = sys.argv[1]


sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

with codecs.open(file_name+'.punkt', 'wb', 'utf-8') as fp:
    for lines in codecs.open(file_name, 'rb', 'utf-8'):
        lines = lines.strip()
        lines = [line_ for line_ in sent_detector.tokenize(lines) if line_]

        for line_ in lines:
            print type(line_)
            fp.writelines(line_+"\n");





































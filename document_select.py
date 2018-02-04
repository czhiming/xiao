#coding:utf-8

import sys
import numpy
import codecs
from nltk.tokenize import word_tokenize

filename = sys.argv[1]

with codecs.open('wiki.en.2000','wb','utf-8') as fp:
    num = 0
    for lines in codecs.open(filename,'rb','utf-8'):
        lines = lines.strip()
        if num >= 2000:
            break
        if numpy.random.randint(2):
            words = word_tokenize(lines)
            print ' '.join(words)
            fp.writelines(' '.join(words)+'\n')
            num += 1
        
        



































#-*- coding:utf8 -*-
'''
Created on 17-9-26

@author: czm
'''
import sys
import json
from nltk.tokenize import word_tokenize
from collections import OrderedDict

filename = sys.argv[1]

def get_dictionary(filepath):
    with open(filepath,"rb") as fp:
        return json.load(fp)

dictionary = get_dictionary('bnc/bnc.large.txt.remove.json')

with open(filename+'.frequency','w') as fp:
    for i,lines in enumerate(open(filename)):
        lines = lines.strip().decode('gbk','ignore')
        #lines = word_tokenize(lines)
        lines = lines.lower()
        lines = lines.split(' ')

        min = 1000000000000
        for word in lines:
            if word in dictionary:
                if dictionary[word] < min:
                    min = dictionary[word]
            else:
                #为出现的词，频率为1
                min = 1
        print "Frequency.py: processed line number %d" % (i+1)
        fp.writelines(str(min)+"\n")

print 'Done.'













if __name__ == '__main__':
    pass

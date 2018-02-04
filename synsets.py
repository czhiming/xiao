#-*- coding:utf8 -*-
'''
Created on 17-9-25

@author: czm
'''
import sys
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
import re
import string
import time

'''
@function: 计算同义词数
@usage: python synsets.py filename
'''


filename = sys.argv[1]

def remove_(lines):
    lines = re.sub(r"\s")

start_time = time.time()

with open(filename+'.synsets','w') as fp:
    for i,lines in enumerate(open(filename)):
        lines = lines.strip().decode('gbk','ignore')
        #lines = ' '.join(word_tokenize(lines))
        #去除标点符号
        lines = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), " ".decode("utf8"), lines)
        lines = lines.split(' ')
        lines = [word for word in lines if len(word)>1]

        sum = 0
        for word in lines:
            total = set([])
            for synset in wn.synsets(word):
                for word in synset.lemma_names():
                    total.add(word)
            sum += len(total)

        print 'Synsets.py: processed lines number %d, synsets sum %d!' % (i+1,sum)
        fp.writelines(str(sum)+"\n")

print "Done."
print 'Time cost: %.2fs' % (time.time() - start_time)





if __name__ == '__main__':
    pass
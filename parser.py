#coding:utf8
import os
import nltk
import sys
from nltk.parse import stanford
from nltk.tokenize import word_tokenize
import time
import codecs

'''
@function: 计算句子的长度，和句法树深度
@usage: python parser.py filename
'''

file_name = sys.argv[1]


parser = stanford.StanfordParser(model_path='edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')
#sentences = parser.raw_parse_sents(("We know it now as masking tape.",\
#        "My Berlin diary for December 2 was limited to four words."))
#result = list(parser.raw_parse("We know it now as masking tape."))

start_time = time.time()


with open(file_name+'.parser','w') as fp:
    for i,lines in enumerate(open(file_name)):
        print 'Parser.py Processing line %d ...' % (i+1)
        lines = lines.strip().decode('gbk','ignore')
        result = list(parser.raw_parse(lines))[0]
        height = result.height()-1


        fp.writelines(str(height)+"\n")

print 'Done.'
print 'Time cost: %.2fs' % (time.time()-start_time)


        

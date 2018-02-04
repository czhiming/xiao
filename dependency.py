#-*- coding:utf8 -*-
'''
Created on 17-9-26

@author: czm
'''
import sys
from nltk.parse.stanford import StanfordDependencyParser
import re
import numpy

'''
@function: 依存句法分析，计算句子依存链长度
@usage: python dependency.py filename
'''

filename = sys.argv[1]


eng_parser = StanfordDependencyParser(model_path='edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')
res = list(eng_parser.parse("A young man and a young woman were sitting behind me .".split()))

print res[0].to_dot()
for row in res[0].triples():
    print row

sys.exit(0)

with open(filename+'.dependency','w') as fp:
    for i,lines in enumerate(open(filename)):
        lines = lines.strip().decode('gbk', 'ignore')
        result = list(eng_parser.raw_parse(lines))[0]
        pattern = re.compile(r'(\d*) -> (\d*)')
        number =  pattern.findall(result.to_dot())

        length = 0
        for j,num in enumerate(number):
            if j == 0: #排除root结点
                pass
            else:
                length += numpy.abs(int(num[0])-int(num[1]))

        print 'Dependency.py: processed line number %d' % (i+1)
        fp.writelines(str(length)+"\n")


if __name__ == '__main__':
    pass

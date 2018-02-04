#-*- coding:utf8 -*-
'''
Created on 17-10-13

@author: czm
'''
import sys

'''
@function: 求句子长度
@usage: python length.py filename
'''

filename = sys.argv[1]

with open(filename+'.length','w') as fp:
    for lines in open(filename):
        lines = lines.strip().split()
        fp.writelines(str(len(lines))+"\n")

print 'length.py Done.'












if __name__ == '__main__':
    pass
#-*- coding:utf8 -*-
'''
Created on 17-10-12

@author: czm
'''

import sys

'''
@function: 两个文件中的值相加
@usage: python add.py file1 file2 file3
'''

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]

fb = open(file2)


with open(file3,'w') as fp:
    for i,lines in enumerate(open(file1)):
        #print "Processing line number %d" % (i+1)
        lines = lines.strip()
        result = int(lines)*0.3 + int(fb.readline().strip())*0.7
        fp.writelines(str(result)+"\n")


fb.close()













if __name__ == '__main__':
    pass

#-*- coding:utf8 -*-
'''
Created on 17-9-26

@author: czm
'''

import sys

filename = sys.argv[1]

with open(filename+'.label','w') as fp:
    for lines in open(filename):
        lines = lines.strip().split()
        label = lines[0]

        fp.writelines(label+"\n")








if __name__ == '__main__':
    pass
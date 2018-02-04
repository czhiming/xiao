#-*- coding:utf8 -*-
'''
Created on 17-9-26

@author: czm
'''

import sys
import json

filename = sys.argv[1]


with open(filename+'.remove','w') as fp:
    for lines in open(filename):
        lines = lines.strip()
        if lines == "":
            pass
        else:
            fp.writelines(lines+"\n")

print "Done."







if __name__ == '__main__':
    pass

#-*- coding:utf8 -*-
'''
Created on Dec 5, 2016

@author: czm
'''

import sys

if len(sys.argv) < 4:
    print 'more than 4 parameters!'
    sys.exit(0)

"""
python combine.py file1 file2 file3 ... output_file
"""
    
file = [open(fp) for fp in sys.argv[1:-1]]

with open(sys.argv[-1],'w') as fp:
    for lines in file[0]:
        lines = lines.strip()
        for i in range(1,len(file)):
            lines = lines+'\t'+file[i].readline().strip()
        fp.writelines(lines+"\n")
    

print "Done."












if __name__ == '__main__':
    pass

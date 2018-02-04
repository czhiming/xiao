#coding:utf8

import sys
import re

p_unit = re.compile('[unit|Unit].*')
p_123 = re.compile('\d*\.\s*.*')
p_section = re.compile('Section.*')
p_listening = re.compile('.*? Listening$')
p_yin = re.compile('^"(.*)"$')
p_123d = re.compile('\d\)\s*.*')
p_abc = re.compile('\w\.\s*.*')

file_name = sys.argv[1]

with open(file_name+'.pre','w') as fp:
    flag = -1
    for i,lines in enumerate(open(file_name)):
        lines = lines.strip()
        if lines == '':
            pass
        elif i == 0:
            pass 
        elif p_unit.match(lines):
            pass
        elif p_123.match(lines):
            pass
        elif p_123d.match(lines):
            pass
        elif p_abc.match(lines):
            pass
        elif p_section.match(lines):
            flag = i
        elif p_listening.match(lines):
            flag = i
        elif i == flag+1:
            flag = -1
        else:
            lines = re.sub('[（(].*[)）]',' ',lines)
            if p_yin.match(lines):
                ss = p_yin.match(lines).groups()[0]
                lines = ss
            lines = lines.split('.')
            
            for line in lines:
                line = line.strip()
                if line != '':
                    if line == '"' or line == '”' or line == "'":
                        pass
                    else:
                        print >> fp,line+'.'




#coding:utf8

import sys


filename = sys.argv[1]

num_tokens = 0
for lines in open(filename):
    lines  = lines.strip().split()
    num_tokens += len(lines)

print num_tokens




























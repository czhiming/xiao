#-*- coding:utf8 -*-
'''
Created on 17-10-12

@author: czm
'''

import sys

'''
@function: 标注一致性，使用kappa系数
@usage: python consistency.py file1 file2
'''


file1 = sys.argv[1]
file2 = sys.argv[2]

fb = open(file2)

a = []
b = []

def PA(a,b):
    sum = 0
    for i,data in enumerate(a):
        if a[i] == b[i]:
            sum += 1;

    return float(sum)/len(a)

def PE(a,b,label):
    sum = 0
    for ll in label:
        sum_a = 0
        sum_b = 0
        for i,data in enumerate(a):
            if a[i] == ll:
                sum_a += 1
            if b[i] == ll:
                sum_b += 1
        sum += sum_a * sum_b

    return float(sum)/len(a)**2

def kappa(a,b,label=[1,2,3]):

    pa = PA(a,b)
    pe = PE(a,b,label)

    return (pa-pe)/(1-pe)

with open(file1) as fp:
    for lines in fp:
        lines = int(lines.strip())
        lines_ = int(fb.readline().strip())
        a.append(lines)
        b.append(lines_)

fb.close()

print "kappa: ",kappa(a,b,label=[1,2,3])

















if __name__ == '__main__':
    pass
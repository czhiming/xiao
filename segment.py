#coding:utf8

import nltk
import codecs

text = codecs.open('one.txt','r','utf8').read()

sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
result = sentence_tokenizer.tokenize(text)

with codecs.open('one.seg.txt','w','utf8') as fp:
    for n,sentence in enumerate(result):
        print >> fp,sentence






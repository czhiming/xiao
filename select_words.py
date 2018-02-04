import gensim
import sys
import numpy
import argparse
from nltk.tag.stanford import StanfordPOSTagger
import codecs
from nltk.tokenize import word_tokenize


filename = sys.argv[1]

model = gensim.models.KeyedVectors.load_word2vec_format('word2vec/model/bnc.large.txt.tok.200.bin',binary=True)
postagger = StanfordPOSTagger('english-bidirectional-distsim.tagger')
#print st.tag("And it doesn't show up on an IQ test .".split())

with codecs.open(filename+'.output', 'wb', 'utf-8') as fp:
    num = 0
    for k,lines in enumerate(codecs.open(filename, 'rb', 'utf-8')):
        
        lines = word_tokenize(lines);
        pos = postagger.tag(lines)
        
        prep_word = None
        for i, word in enumerate(pos):
            if word[1] == u'IN':
                prep_word = word[0]
                idx = i
        
        if prep_word != None:
            print lines
            fp.writelines(' '.join(lines)+'\n')
            num += 1
        
        if num > 100:
            break
            """
            real_answer = lines[idx]
            #real_idx = numpy.random.ranint(4)
            
            lines[idx] = u'____' 
            question = ' '.join(lines)
            answers = model.most_similar(prep_word)
            print prep_word
            for word in answers:
                print word
            fp.writelines(question+' ('+real_answer+')'+'\n')
            
            result = [answers[0][0],answers[1][0],answers[2][0],real_answer]
            numpy.random.shuffle(result)
            
            options = ['A.','B.','C.','D.']
            for i,res in enumerate(result):
                fp.writelines('\t'+options[i]+' '+res.lower()+'\n')
            fp.writelines('\n');
            """
            
            
            
            
            
            
            

#coding:utf8


from nltk.tag.stanford import StanfordPOSTagger

st = StanfordPOSTagger('english-bidirectional-distsim.tagger')
print st.tag("And it doesn't show up on an IQ test .".split())









#!/bin/sh

root='/home/czm/workspace/rnnlm-0.3e'
model='rnnlm'

filename=$1

#-----wmt16-----
$root/rnnlm -rnnlm $model/bnc.rnnlm.model -test $filename -nbest -debug 0 > $filename.rnnlm
print 'Done.'






#!/bin/sh

filename=$1
lng=en


#./tokenizer.perl -a -l $lng < $filename > $filename.tok
#filename=$filename.tok
:<<!
python length.py $filename
python parser.py $filename
python synsets.py $filename
python dependency.py $filename
python frequency.py $filename
echo "run ./rnnlm.sh"
./rnnlm.sh $filename
!

python combine.py $filename.length $filename.parser $filename.synsets \
    $filename.dependency $filename.frequency $filename.rnnlm $filename.features

#python combine.py $filename.length $filename.parser \
#    $filename.rnnlm $filename.features

:<<!
rm -f $filename.length
rm -f $filename.parser
rm -f $filename.synsets
rm -f $filename.dependency
rm -f $filename.frequency
rm -f $filename.rnnlm
!























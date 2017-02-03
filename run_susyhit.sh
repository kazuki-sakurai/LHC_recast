#!/bin/bash

echo "#--- Start of run_susyhit.sh ---#"

wdir=`pwd`
susyhit_dir=$wdir/susyhit

tag=`echo $1 | sed -e "s/\.slha//"`
slha_file=$tag.slha

if [[ ! -e $slha_file ]]; then
    echo "SLHA file " $slha_file " does not exist"
    exit
fi

rm -f $susyhit_dir"/slhaspectrum.in"
cp $slha_file $susyhit_dir"/slhaspectrum.in"
cd $susyhit_dir
./run
cp susyhit_slha.out $wdir/result/$tag.spcdec
cd $wdir

echo "tail "$tag".spcdec"
tail result/$tag.spcdec
echo "#--- End of run_susyhit.sh ---#"

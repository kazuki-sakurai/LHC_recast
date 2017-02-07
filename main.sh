#!/bin/bash

wdir=`pwd`
xsecs_main=$wdir'/cross-section/read_XSfb_from_pythia_out.py'

mode='all'
energy='13'
nev='5000'

tag=`echo $1 | sed -e "s/\.slha//"`
slha_file=$tag.slha

if [[ ! -e $slha_file ]]; then
    echo "SLHA file " $slha_file " does not exist"
    exit
fi

#---- calculate decay table 
sh run_susyhit.sh $tag.slha   # > generates $tag.spcdec

#---- event generation 
sh run_pythia.sh $tag.spcdec $mode $energy $nev # > generates $tag.hepmc, $tag.pythia_out

#---- detector simulation 
sh run_delphes.sh $tag.hepmc  # > generates $tag.lhco

#---- event analysis 
sh run_analysis.sh $tag.lhco  # > generates $tag.eff

#---- cross-section 
pythia_out_path=$wdir'/result/'$tag'.pythia_out'
XSfb=`$xsecs_main $pythia_out_path`
echo 'Cross-Section: '$XSfb' [fb]'

#---- statistics 
sh run_statistics.sh $tag.eff $XSfb # > generates $tag.stats


exit
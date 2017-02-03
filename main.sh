#!/bin/bash

wdir=`pwd`

tag=`echo $1 | sed -e "s/\.slha//"`
slha_file=$tag.slha

if [[ ! -e $slha_file ]]; then
    echo "SLHA file " $slha_file " does not exist"
    exit
fi

#---- calculate decay table 
sh run_susyhit.sh $tag.slha   # > generates $tag.spcdec

#---- event generation 
sh run_pythia.sh $tag.spcdec  # > generates $tag.hepmc, $tag.pythia_out

#---- detector simulation 
sh run_delphes.sh $tag.hepmc  # > generates $tag.lhco

#---- event analysis 
sh run_analysis.sh $tag.lhco  # > generates $tag.eff

#---- statistics 
sh run_statistics.sh $tag.eff  # > generates $tag.stats


exit
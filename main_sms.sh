#!/bin/bash

wdir=`pwd`

mode=$1 # [QqN1, GqqN1]
m_heavy=$2
m_lsp=$3

energy='13'
lumi='3.2'
nev_min='5000'

tag=$mode'_'$m_heavy'_'$m_lsp

#---- calculate decay table 
python $wdir'/for_sms/write_specdec_'$mode'.py' $m_heavy $m_lsp > $wdir'/result/'$tag.spcdec   # > generates $tag.spcdec

#---- cross-section
XSfb=`$wdir'/cross-section/read_XSfb_from_data.py' $mode  $m_heavy  $energy`
echo 'Cross-Section: '$XSfb' [fb]'
nev=`$wdir/cross-section/get_nev.py $XSfb $lumi $nev_min`
echo 'Nev: '$nev

#---- event generation 
sh run_pythia.sh $tag.spcdec $mode $energy $nev # > generates $tag.hepmc, $tag.pythia_out

#---- detector simulation 
sh run_delphes.sh $tag.hepmc  # > generates $tag.lhco

#---- event analysis 
sh run_analysis.sh $tag.lhco  # > generates $tag.eff

#---- statistics 
sh run_statistics.sh $tag.eff $XSfb # > generates $tag.stats


exit
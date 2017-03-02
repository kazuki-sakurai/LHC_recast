#!/bin/bash

wdir=`pwd`

mode=$1 # [QqN1, GqqN1, GttN1, GqqN2lLlN1]
if [ $mode == 'QqN1' ] || [ $mode == 'GqqN1' ] || [ $mode == 'GttN1' ]; then
    n_mass=2
    m1=$2
    m2=$3
    tag=$mode'_'$m1'_'$m2
fi
if [[ $mode == 'GqqN2lLlN1' ]]; then
    n_mass=4
    m1=$2
    m2=$3
    m3=$4
    m4=$5        
    tag=$mode'_'$m1'_'$m2'_'$m3'_'$m4    
fi
if [ $mode == 'C1lLlN1_N2lLlN1' ] || [ $mode == 'C1lLlN1_C1lLlN1' ] || [ $mode == 'C1lL3lN1_N2lL3lN1' ] || [ $mode == 'GqqC1wN1' ]; then
    n_mass=3
    m1=$2
    m2=$3
    m3=$4
    tag=$mode'_'$m1'_'$m2'_'$m3    
fi

energy='13'
lumi='3.2'
nev_min='5000'

#---- calculate decay table 
if [[ $n_mass == 2 ]]; then
    python $wdir'/for_sms/write_specdec_'$mode'.py' $m1 $m2 > $wdir'/result/'$tag.spcdec   # > generates $tag.spcdec
fi
if [[ $n_mass == 3 ]]; then
    python $wdir'/for_sms/write_specdec_'$mode'.py' $m1 $m2 $m3 > $wdir'/result/'$tag.spcdec   # > generates $tag.spcdec
fi
if [[ $n_mass == 4 ]]; then
    python $wdir'/for_sms/write_specdec_'$mode'.py' $m1 $m2 $m3 $m4 > $wdir'/result/'$tag.spcdec   # > generates $tag.spcdec
fi

#---- cross-section
XSfb=`$wdir'/cross-section/read_XSfb_from_data.py' $mode  $m1 $energy`
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
#!/bin/bash

wdir=`pwd`

if [[ $3 == '' ]]; then
    echo '[mode] [m1] [m2] ...'
    exit
fi
mode=$1 # [QqN1, GqqN1, GttN1, GqqN2lLlN1]

event_generator='pythia'
if [[ $mode == 'C1wlepN1_N2zlepN1' ]] || [[ $mode == 'C1whadN1_N2zlepN1' ]]; then
    event_generator='madgraph'
fi

if [ $mode == 'QqN1' ] || [ $mode == 'B1bN1' ] || [ $mode == 'GqqN1' ] || [ $mode == 'GttN1' ] || [ $mode == 'GbbN1' ] || [ $mode == 'LlN1' ] || [ $mode == 'C1whadN1_N2zlepN1' ] || [ $mode == 'C1wlepN1_N2zlepN1' ]; then
    n_mass=2
    m1=$2
    m2=$3
    tag=$mode'_'$m1'_'$m2
fi
if [ $mode == 'GqqN2lLlN1' ] || [ $mode == 'GqqC1wN2zN1' ]; then
    n_mass=4
    m1=$2
    m2=$3
    m3=$4
    m4=$5        
    tag=$mode'_'$m1'_'$m2'_'$m3'_'$m4    
fi
if [ $mode == 'T1bC1wN1' ] || [ $mode == 'C1lLlN1_N2lLlN1' ] || [ $mode == 'C1lLlN1_C1lLlN1' ] || [ $mode == 'C1lL3lN1_N2lL3lN1' ] || [ $mode == 'GqqC1wN1' ] || [ $mode == 'B1tC1wN1' ]; then
    n_mass=3
    m1=$2
    m2=$3
    m3=$4
    tag=$mode'_'$m1'_'$m2'_'$m3    
fi

xs_flag='read_from_table'
if [ $mode == 'LlN1' ]; then
    xs_flag='read_from_pythia'
    nev='100000'
    if [ $m1 -gt 100 ]; then 
        nev='50000' 
    fi
    if [ $m1 -gt 200 ]; then 
        nev='10000' 
    fi
    if [ $m1 -gt 300 ]; then 
        nev='5000' 
    fi
fi


energy='13'
lumi='36'
nev_min='2000'

#---- calculate decay table
if [[ $event_generator == 'pythia' ]]; then 
    if [[ $n_mass == 2 ]]; then
        python $wdir'/for_sms/write_specdec_'$mode'.py' $m1 $m2 > $wdir'/result/'$tag.spcdec   # > generates $tag.spcdec
    fi
    if [[ $n_mass == 3 ]]; then
        python $wdir'/for_sms/write_specdec_'$mode'.py' $m1 $m2 $m3 > $wdir'/result/'$tag.spcdec   # > generates $tag.spcdec
    fi
    if [[ $n_mass == 4 ]]; then
        python $wdir'/for_sms/write_specdec_'$mode'.py' $m1 $m2 $m3 $m4 > $wdir'/result/'$tag.spcdec   # > generates $tag.spcdec
    fi
fi
if [[ $event_generator == 'madgraph' ]]; then 
    if [[ $n_mass == 2 ]]; then
        python $wdir'/for_sms/write_param_'$mode'.py' $m1 $m2 > $wdir'/result/'$tag.param   # > generates $tag.spcdec
    fi    
fi


#---- cross-section
if [ $xs_flag == 'read_from_table' ]; then
    br='1'
    if [[ $mode == 'C1wlepN1_N2zlepN1' ]]; then
        br='0.01446'  #BR_zlep = 0.03363*2, BR_wlep = 0.215
    fi
    if [[ $mode == 'C1whadN1_N2zlepN1' ]]; then
        br='0.04547'  #BR_zlep = 0.03363*2, BR_whad = 0.676
    fi    
    XSfb=`$wdir'/cross-section/read_XSfb_from_data.py' $mode  $m1 $energy $br`
    echo 'Cross-Section: '$XSfb' [fb]'
    nev=`$wdir/cross-section/get_nev.py $XSfb $lumi $nev_min`
    echo 'Nev: '$nev
fi

#---- event generation 
if [[ $event_generator == 'pythia' ]]; then 
    sh run_pythia.sh $tag.spcdec $mode $energy $nev # > generates $tag.hepmc, $tag.pythia_out

    if [ $xs_flag == 'read_from_pythia' ]; then
        XSfb=`$wdir/cross-section/read_XSfb_from_pythia_out.py $wdir/result/$tag.pythia_out`
        echo 'Cross-Section: '$XSfb' [fb]'        
    fi
fi
if [[ $event_generator == 'madgraph' ]]; then 
    sh run_madgraph.sh $tag $mode $energy $nev # > generates $tag.hepmc, $tag.pythia_out
fi

#---- detector simulation 
sh run_delphes.sh $tag.hepmc  # > generates $tag.lhco

#---- event analysis 
sh run_analysis.sh $tag.lhco  # > generates $tag.eff

#---- statistics 
XS_err='0.1'
sh run_statistics.sh $tag.eff $XSfb $XS_err # > generates $tag.stats


exit
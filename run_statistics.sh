#!/bin/bash

echo "#--- Start of run_statistics.sh ---#"
wdir=`pwd`
statistics_main=$wdir'/statistics/statistics_main.py'
xsec_main=$wdir'/statistics/read_XSfb_from_pythia_out.py'

tag=`echo $1 | sed -e "s/\.eff//"`
pythia_out_path=$wdir/result/$tag.pythia_out
eff_path=$wdir/result/$tag.eff
stats_out=$wdir/result/$tag.stats

if [[ -e $stats_out ]]; then
    rm -f $stats_out
fi

XS_in_fb=`$xsec_main $pythia_out_path`
#echo $XS_in_fb

$statistics_main  $XS_in_fb  $eff_path  | tee $stats_out 
ls  -ltr  $stats_out

echo "#--- End of run_statistics.sh ---#"

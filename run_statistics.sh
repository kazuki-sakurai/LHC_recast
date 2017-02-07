#!/bin/bash

echo "#--- Start of run_statistics.sh ---#"
wdir=`pwd`
statistics_main=$wdir'/statistics/statistics_main.py'

tag=`echo $1 | sed -e "s/\.eff//"`
pythia_out_path=$wdir/result/$tag.pythia_out
eff_path=$wdir/result/$tag.eff
stats_out=$wdir/result/$tag.stats

XS_in_fb=$2

if [[ -e $stats_out ]]; then
    rm -f $stats_out
fi

$statistics_main  $XS_in_fb  $eff_path  | tee $stats_out 
ls  -ltr  $stats_out

echo "#--- End of run_statistics.sh ---#"

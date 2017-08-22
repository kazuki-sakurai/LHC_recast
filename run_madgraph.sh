#!/bin/bash

wdir=`pwd`


tag=$1
mode=$2
energy=$3
nev=$4

master_mg5dir=$wdir'/for_madgraph/mg5_'$mode

mg5_work=$wdir'/result/mg5work_'$tag
pythia8_card=$wdir'/for_madgraph/pythia8_card.dat'
proc_card=$wdir'/for_madgraph/proc_card_'$mode.dat
madspin_card=$wdir'/for_madgraph/madspin_'$mode.dat
param_card=$wdir'/result/'$tag.param
me5_card=$wdir'/for_madgraph/me5_configuration.txt'

echo 'master directory ' $master_mg5dir
if [[ ! -d $master_mg5dir ]]; then
    echo $master_mg5dir' does not exit !!'
    echo 'We will create it.'
    $MG5_PATH < $proc_card
fi

if [[ -d $mg5_work ]]; then
    echo 'removing existing directory '$mg5_work
    rm -rf $mg5_work
fi
cp -r $master_mg5dir $mg5_work
cp $param_card $mg5_work'/Cards/param_card.dat'
cp $pythia8_card $mg5_work'/Cards/pythia8_card.dat'
cp -f $me5_card $mg5_work'/Cards/me5_configuration.txt'
# echo cp $pythia8_card $mg5_work'/Cards/pythia8_card.dat'
# less $pythia8_card
# less $mg5_work'/Cards/pythia8_card'
# ls -ltr $mg5_work'/Cards/'
# exit
cp $madspin_card $mg5_work'/Cards/madspin_card.dat'
python $wdir'/for_madgraph/write_run_card.py' $energy $nev > $mg5_work'/Cards/run_card.dat'

echo $mg5_work
cd $mg5_work
ls bin
./bin/generate_events < $wdir'/for_madgraph/exe.dat'
gunzip $mg5_work'/Events/run_01_decayed_1/tag_1_pythia8_events.hepmc.gz'
cp $mg5_work'/Events/run_01_decayed_1/run_01_decayed_1_tag_1_banner.txt' $wdir'/result/'$tag.banner
mv $mg5_work'/Events/run_01_decayed_1/tag_1_pythia8_events.hepmc' $wdir'/result/'$tag.hepmc

exit

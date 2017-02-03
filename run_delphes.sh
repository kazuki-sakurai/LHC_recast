#!/bin/bash

echo "#--- Start of run_delphes.sh ---#"

wdir=`pwd`
delphes_dir='/Users/kazuki/Packages/Delphes-3.3.2'
delphes=$delphes_dir'/DelphesHepMC'
root2lhco=$delphes_dir'/root2lhco'
detector_card=$wdir/for_delphes/delphes_card_ATLAS.tcl

tag=`echo $1 | sed -e "s/\.hepmc//"`
hepmc_path=$wdir/result/$tag.hepmc
root_output=$wdir/result/$tag.root
lhco_output=$wdir/result/$tag.lhco

if [[ ! -e $hepmc_path ]]; then
    echo "HepMC file " $hepmc_path " does not exist"
    exit
fi

if [[ ! -e $detector_card ]]; then
    echo "Detector Card " $detector_card " does not exist"
    exit
fi

if [[ -e $root_output ]]; then
    rm -f $root_output
fi

if [[ -e $lhco_output ]]; then
    rm -f $lhco_output
fi

$delphes  $detector_card  $root_output  $hepmc_path
ls -ltr $root_output

$root2lhco $root_output $lhco_output
ls -ltr $lhco_output

echo "#--- End of run_delphes.sh ---#"

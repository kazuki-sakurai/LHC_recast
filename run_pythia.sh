#!/bin/bash
echo "#--- Start of run_pythia.sh ---#"

wdir=`pwd`
pythia=$PYTHIA_PATH
input_writer='for_pythia/write_pythia_input.py'

tag=`echo $1 | sed -e "s/\.spcdec//"`
input_path=$wdir/result/$tag.spcdec
pythia_setting=$wdir/result/$tag.pythia_input
hepmc_output=$wdir/result/$tag.hepmc
pythia_writeout=$wdir/result/$tag.pythia_out

if [[ ! -e $input_path ]]; then
    echo "input file " $input_path " does not exist"
    exit
fi

if [[ -e $hepmc_output ]]; then
    rm -f $hepmc_output
fi


nev='5000'
python $input_writer  $input_path  $nev  >  $pythia_setting

$pythia  $pythia_setting  $hepmc_output | tee  $pythia_writeout
ls -ltr $hepmc_output

echo "#--- End of run_pythia.sh ---#"

exit
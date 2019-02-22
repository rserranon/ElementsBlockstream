#!/bin/bash
# run from terminal as: source create_aliases.sh
# execute bash script line by line
set -x
#trap read debug

# This code is based upon and expands the example found here: https://github.com/ElementsProject/elements/tree/elements-0.14.1/contrib/assets_tutorial

################################
#
# To run this code just open a terminal in your home directory and run:
# bash runtutorial.sh
#
# Then press the return key to execute each line in turn.
#
# If you want to run some of the steps automatically and then have execution stop
# and wait for you to press enter before continuing one line at a time: move 
# the **trap read debug** statement down so that it is above the line you want to 
# stop at. Execution will run each line automatically and stop when that line is 
# reached. It will then switch to executing one line at a time, waiting for you 
# to press return before executing the next command.
# 
# You will see that occasionally we will use the **sleep** command to pause execution.
# This allows the daemons time to do things like stop, start and sync mempools.
# 
# It is perhaps a good idea to have the relevant tutorial pages open as you run 
# through this code for reference, as it is not itself annotated in any meaningful way.
#
# There is a chance that the " and ' characters may not paste into your 
# **runtutorial.sh** file correctly, so type over them yourself if you come 
# across any issues executing the code.
#
#################################

#cd
cd elements_bash_scripts

shopt -s expand_aliases

alias b-dae="bitcoind -datadir=$HOME/bitcoindir"
alias b-cli="bitcoin-cli -datadir=$HOME/bitcoindir"

alias e1-dae="$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1"
alias e1-cli="$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1"

alias e2-dae="$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2"
alias e2-cli="$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2"


alias
set +x
echo "Completed"

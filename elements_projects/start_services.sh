#!/bin/bash
# run from terminal as: source create_aliases.sh
echo "Start Services"
b-dae 
e1-dae 
e2-dae 
ps -A | grep bitcoind
ps -A | grep elementsd
echo "Services Started:"
echo "Get Info"
b-cli -getinfo
e1-cli getwalletinfo
e2-cli getwalletinfo

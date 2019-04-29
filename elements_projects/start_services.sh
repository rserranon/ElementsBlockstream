#!/bin/bash
# run from terminal as: source create_aliases.sh
echo "Start Services"
b-dae
e1-dae
e2-dae
ps -A | grep bitcoind
ps -A | grep elementsd
echo "Services Started:"
echo "Get Info\n"
echo "Get Info: Bitcoin"
b-cli -getinfo
echo "\nGet Wallet Info: Elements 1"
e1-cli getwalletinfo
echo "\nGet Wallet Info: Elements 2"
e2-cli getwalletinfo

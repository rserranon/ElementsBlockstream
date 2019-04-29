#!/bin/bash
# reset bitcoin and elements data by deleting directories
#
rm -r ~/bitcoindir
rm -r ~/elementsdir1
rm -r ~/elementsdir2
mkdir ~/bitcoindir
mkdir ~/elementsdir1
mkdir ~/elementsdir2
#
cp ~/elements/contrib/assets_tutorial/bitcoin.conf ~/bitcoindir/bitcoin.conf
cp ~/elements/contrib/assets_tutorial/elements1.conf ~/elementsdir1/elements.conf
cp ~/elements/contrib/assets_tutorial/elements2.conf ~/elementsdir2/elements.conf

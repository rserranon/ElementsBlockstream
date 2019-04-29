#!/bin/bash
# run from terminal as: source create_aliases.sh
echo "Stopping Services"
b-cli stop
e1-cli stop
e2-cli stop
echo "Services Stopped"

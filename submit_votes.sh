#!/bin/bash

cd ~/Documents/Programming/Python
COUNTER=71
until [  $COUNTER -lt 1 ]; do
	python vote_marianna.py
	echo COUNTER $COUNTER
	let COUNTER-=1
done

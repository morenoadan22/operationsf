#!/bin/bash

COUNTER=87
until [  $COUNTER -lt 1 ]; do
	python vote_marianna.py	
	echo counter $COUNTER
	let COUNTER-=1
done

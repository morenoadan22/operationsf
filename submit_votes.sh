#!/bin/bash

COUNTER=20
until [  $COUNTER -lt 1 ]; do
	python vote_marianna.py
	echo COUNTER $COUNTER
	let COUNTER-=1
done

#!/bin/bash

COUNTER=94
until [  $COUNTER -lt 1 ]; do
	python vote_marianna.py	
	let COUNTER-=1
done

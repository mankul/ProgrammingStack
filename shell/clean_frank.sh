#!/bin/bash

for dirName in $@
do
	rm -r "$dirName"{1..4} 2> /dev/null
done



#!/bin/bash

echo "all counts $#"
for item in $@
do
	echo "$item"
	mkdir -p "$item"{1..4} 2> /dev/null
done
# > /dev/null 2> /dev/null
echo "function call $1"

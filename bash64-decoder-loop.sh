#!/usr/bin/bash

file=$1
read=$(cat $file)

for i in $(seq 1 13)
do
	read=$(echo ${read} | tr -d ' ' | base64 -d 2>/dev/null)
done

echo ${read} 

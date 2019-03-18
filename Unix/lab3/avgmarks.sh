#!/bin/sh
echo "Enter Unix, Java and DSA marks out of 100:"
read u 
read j 
read d
avg=$(echo "scale=1; ($u + $j + $d) / 3" | bc)
if (( $(echo "$avg >= 70" | bc -l) )); then
	echo "Distinction"
elif (( $(echo "$avg >= 60" | bc -l) )); then
	echo "First class"
elif (( $(echo "$avg >= 50" | bc -l) )); then
	echo "Second class"
elif (( $(echo "$avg >= 40" | bc -l) )); then
	echo "Third class"
else
	echo "Fail"
fi
#!/bin/bash
echo "Enter file1"
read f1
echo "Enter file2"
read f2

if [ -f $f1 ] && [ -f $f2 ]
then
str=`comm -3 $f1 $f2`
if [ ${#str} = 0 ]
then echo "Files are equal"
else
	echo "Files are not equal"
echo
echo "The common elements of file are:"
comm -12 $f1 $f2
echo
echo "The unique elements of file 1 are:"
comm -23 $f1 $f2
echo
echo "The unique elements of file 2 are:"
comm -13 $f1 $f2
echo
echo "Steps to convert $f1 to $f2 are:"
diff $f1 $f2
fi
else
	echo "Invalid inputs"
fi
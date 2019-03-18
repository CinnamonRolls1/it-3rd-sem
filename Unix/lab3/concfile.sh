#!/bin/sh
e1=0
e2=0
echo "Enter name of first file:"
read f1
if [ -f "$f1" ]; then
	echo "File exists"
	e1=1
else
	echo "File doesn't exist"
fi

echo "Enter name of second file:"
read f2
if [ -f "$f2" ]; then
	echo "File exists"
	e2=1
else
	echo "File doesn't exist"
fi

if [ $e1 -eq 1 ] && [ $e2 -eq 1 ]
then
	echo "Appending..."
	cat "$f1" >> "$f2"
	cat "$f2"
fi



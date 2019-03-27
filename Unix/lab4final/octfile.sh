#!/bin/sh

echo "Enter file name:"
read name

if [ -f "$name" ]
then
	echo "$name found!"

	echo "Original file:"
	echo

	cat "$name"

	echo
	echo "File after conversion to octal:"
	echo

	od "$name"
else
	echo "$name not found in this directory."
fi


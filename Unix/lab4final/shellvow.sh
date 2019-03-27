#!/bin/sh

echo "Current shell is $SHELL"
echo "All files in directory:"
ls -p | grep -v /
echo
echo "Files not starting with vowels:"
ls -p | grep -v / | grep -v '^[AaEeIiOoUu]'
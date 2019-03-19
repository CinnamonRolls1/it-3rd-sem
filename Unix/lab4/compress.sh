#!/bin/sh

echo "Creating files..."
>f1.txt
>f2.txt
>f3.txt
>f4.txt

echo "Creating folder..."
mkdir folder

echo "Moving files to folder..."
mv f1.txt folder
mv f2.txt folder
mv f3.txt folder
mv f4.txt folder

echo "Compressing..."
tar -zcvf folder.tar.gz folder

gzip -l folder.tar.gz




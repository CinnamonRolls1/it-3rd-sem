#redo the whole thing with each file receiving a multiline strings and then comparings files line by line


#!/bin/sh
echo 'Enter string 1'
read s1
#s1='hello world'
#echo "$s1"

echo 'Enter string 2'
read s2
#s2='hello perfect world'
#echo "$s2"

echo "$s1" > file1.txt
echo "$s2" > file2.txt

echo 'Comparison:'
cmp file1.txt file2.txt | tee cmpmsg.txt
val=$(cat cmpmsg.txt | tail -c +34 | head -c 1)



echo
echo 'Common element:'


##all common characters but sorted

#fold -w1 file1.txt | sort > f1.txt
#fold -w1 file2.txt | sort > f2.txt  
#comm -12 f1.txt f2.txt | tr -d '\n> ' 


##first n common characters
head -c $(echo "$val - 1" | bc) file1.txt | tee common.txt 



echo
echo 'Elements unique to first file:'
#comm -1 file1.txt file2.txt
tail -c $(echo "+$(echo "$val" | bc)") file1.txt

echo
echo 'Elements unique to second file:'
#comm -2 file1.txt file2.txt
tail -c $(echo "+$(echo "$val" | bc)") file2.txt

echo
echo 'Making files identical:'
cp -f common.txt file1.txt
cp -f common.txt file2.txt 
echo 'File one:'
cat file1.txt
echo
echo 'File two:'
cat file2.txt
echo
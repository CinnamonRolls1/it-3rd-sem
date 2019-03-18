#!/bin/sh



echo "Enter file name"
read name

#files=$(dir -F -A ) #| tr ' ' '\n')
#echo "$files"
#flist=$(grep -e -i -f $name $files)
#echo "flist: $flist"

#while IFS= read -r var
#do
  #echo "contents of $var"
  #cat var
#done < "$flist"
if [ -f "$name" ]
then
	echo "$name is a file"
	
	cat "$name"
elif [ -d "$name" ]
then
	echo "$name is a directory"
	adr=$(echo "$PWD/$name/*")
	for file in $adr
	do
		echo "$file"
	done
fi
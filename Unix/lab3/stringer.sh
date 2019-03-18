#!/bin/sh
echo "Enter first string: "
read s1
echo "Enter second string: "
read s2
rev2=$(echo $s2 | rev)
#rev2 = $(rev<<<"$s2")

case "$s1" in
	'')
		if [ "$s2" == '' ]
		then
			echo "Both strings are empty"
		fi
		;;
	$s2)
		echo "Strings are same"
		;;
	$rev2)
		echo "Strings are palidromes"
		;;
esac
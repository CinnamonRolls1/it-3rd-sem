#!1/bin/sh
declare -a arr
echo "Enter 5 numbers:"
i=1
max=0
dup=0
temp=0
read min
arr[0]=$min
max=$min
while [ $i -lt 5 ]
do
	read temp
	arr[i]=$temp
	if [ $temp -gt $max ]
	then
		max=$temp
	fi
	if [ $temp -lt $min ]
	then
		min=$temp
	fi
	i=$(echo "scale=0; $i + 1" | bc)
done
echo "max is $max"
echo "min is $min"
len=${#arr[*]}
#sarr=($(echo "${arr[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))
sarr=($(printf "%s\n" "${arr[@]}" | sort -u)); echo "${sarr[@]}"
if [ ${#sarr[*]} -lt $len ]
then
	dup=$(echo "scale=0; ${#arr[*]} - ${#sarr[*]}" | bc)
	echo "$dup duplicate(s) made"
fi

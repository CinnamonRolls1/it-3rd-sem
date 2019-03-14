#1/bin/sh
i=0
lt=0
gt=0
z=0
declare -a arr
declare -a newarr
echo "Enter 10 numbers"
while [ $i -lt 10 ]
do
	read inp
	arr[i]=$inp
	if [ $inp -lt 0 ]
	then
		lt=$(echo "scale=0; $lt + 1" | bc)
	elif [ $inp -gt 0 ]
	then 
		gt=$(echo "scale=0; $gt + 1" | bc)
	else
		z=$(echo "scale=0; $z + 1" | bc)
	fi
	i=$(echo "scale=0; $i + 1" | bc)
done
newarr=($(echo "${arr[*]}" | sort -n ))
echo "${newarr[*]}"
echo "negative numbers : $lt"
echo "positive numbers : $gt"
echo "zeros : $z"


	
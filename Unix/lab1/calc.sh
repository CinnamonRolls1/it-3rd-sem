#1/bin/sh
echo "enter first number"
read a
echo "enter second number"
read b
echo "enter operator"
read o
if [ "$o" = "+" ]
then
	sum=$(echo "scale=2; $a + $b" | bc)
	echo "$sum"
elif [ "$o" = '-' ]
then
	dif=$(echo "scale=2; $a - $b" | bc)
	echo "$dif"
elif [ "$o" = '*' ]
then
	prod=$(echo "scale=2; $a * $b" | bc)
	echo "$prod"
elif [ "$o" = '/' ]
then
	quot=$(echo "scale=2; $a / $b" | bc)
	echo "$quot"
else
	echo "invalid operator"
fi

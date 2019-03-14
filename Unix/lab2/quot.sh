#1/bin/sh
big=0
sml=0
while true
do
	echo "enter first number"
	read a
	echo "enter second number"
	read b
	if [ $a -le 0 ] || [ $b -le 0 ]
	then
		echo "invalid input, try again:"
	else
		break
	fi
done

if [ $a -lt $b ]
then
	sml=$a
	big=$b
else
	big=$a
	sml=$b
fi
quot=$(echo "scale=3; $sml / $big" | bc)
echo "$quot"
#1/bin/sh
echo 'enter number'
read n
i=1
f=0
while [ $i -le $n ]
do
	f=$(echo "scale=2; $f + $i" | bc)
	i=$(echo "scale=2; $i + 1" | bc)
done
echo "sum: $f"


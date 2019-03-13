#1/bin/sh
echo "Enter set length"
read n
i=0
t=0
while [ $i -lt $n ]
do
	read n1
	t=$(echo "scale=2; $t + $n1" | bc)
	i=$(echo "scale=2; $i + 1" | bc)
done
avg=$(echo "scale=2; $t / $n" | bc)
echo "average= $avg"


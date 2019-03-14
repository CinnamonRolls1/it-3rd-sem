#1/bin/sh
i=1
echo "CALCULATING..."
while [ $i -le 999 ]
do
	m=$i
	n=$m
	s=0
	d=0
	while [ $m -gt 0 ]
	do
		d=$(echo "scale=0; $m%10" | bc)
		s=$(echo "scale=0; $s + ($d * $d * $d)" | bc)
		m=$(echo "scale=0; $m / 10" | bc)
	done
	if [ $s -eq $n ]
	then
		echo "$i"
	fi
	i=$(echo "scale=0; $i+1" | bc)
done
echo "Finished!"

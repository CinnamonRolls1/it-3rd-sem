#incomplete

#!/bin/sh
declare -A mat
echo 'Enter no of values in diagonal:'
read n
echo 'Enter values:'
for (( i = 0; i < $n; i++ )); do
	for (( j = 0; j < $n; j++ )); do
		if [[ $i -eq $j ]]; then
			read val
			mat[$i,$j]=$val
		else
			mat[$i,$j]=0
		fi
	done
done

for (( i = 0; i < $n; i++ )); do
	for (( j = 0; j < $n; j++ )); do
		echo -n "${mat[$i,$j]} "
	done
	echo
done
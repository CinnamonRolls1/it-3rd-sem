#!/bin/sh
declare -A mat1
declare -A mat2
echo 'MATRIX1
______________________'
echo 'Enter no of rows:'
read m
echo 'Enter no of columns:'
read n

echo 'Enter values'
for (( i = 0; i < m; i++ )); do
	echo "Row $i"
	for (( j = 0; j < n; j++ )); do
		read val
		mat1[$i,$j]=$val
	done
done

echo 'MATRIX2
______________________'

echo 'Enter values'
for (( i = 0; i < m; i++ )); do
	echo "Row $i"
	for (( j = 0; j < n; j++ )); do
		read val
		mat2[$i,$j]=$val
	done
done

echo "Addition"
for (( i = 0; i < m; i++ )); do
	for (( j = 0; j < n; j++ )); do
		echo -n $(echo "${mat1[$i,$j]} + ${mat2[$i,$j]}" | bc)
		echo -n " "
	done
	echo
done
#1/bin/sh
echo "length"
read l
echo "breadth"
read b
area=$(echo "scale=2; $l * $b" | bc)
echo "$area"

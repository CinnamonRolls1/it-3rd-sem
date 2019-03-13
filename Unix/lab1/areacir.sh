#1/bin/sh
echo 'enter radius'
read r
area=$(echo "scale=2;3.14 * ($r * $r)" | bc)
echo "area : $area"

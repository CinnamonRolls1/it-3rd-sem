#!/bin/sh
echo "
Choose:
[1] Decimal -> Binary
[2] Binary  -> Decimal
[3] Binary  -> Hex
[4] Hex     -> Decimal"
read ch 
echo "Enter number"
read n 
case $ch in
	"1")
		echo "obase=2;ibase=10; $n"|bc
		;;
	"2")
		echo "obase=10;ibase=2; $n"|bc
		;;
	"3")
		echo "obase=16;ibase=2; $n"|bc
		;;
	"4")
		echo "obase=2;ibase=16; $n"|bc
		;;
	*)
		echo "Invalid choice"
esac
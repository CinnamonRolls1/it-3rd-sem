#1/bin/sh
echo "enter initial deposit"
read p
echo "enter interest rate per annum"
read r
echo "enter no. of years"
read t
i=`expr $p \* $r \* $t / 100`
echo "simple interest: $i"





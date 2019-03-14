#1/bin/sh
echo "Current working directory:"
pwd
echo
echo "Current username:"
whoami
echo
DATE=`date +%m/%d/%y`
echo "Today is $DATE"
echo 
echo "No of users logged in:"
users | wc -w
echo
echo "Terminal:"
tty



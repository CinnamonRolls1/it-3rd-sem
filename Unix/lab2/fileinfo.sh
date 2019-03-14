#!1/bin/sh
files=$(ls -p | grep -v / | wc -w)

dire=$(ls -p | grep / | wc -w)

	

echo "$dire directories found"
echo "$files files found"
echo

if [ $dire != 0 ]
then
	echo "Directories: "
	ls -p | grep /
fi
echo

if [ $files != 0 ]
then
	echo "Files: "
	ls -p | grep -v /
fi


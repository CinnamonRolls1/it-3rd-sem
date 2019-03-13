def fib(n):
	a=0
	b=1
	print(a)
	print(b)
	for i in range(1,n):
		c=a+b
		a=b
		
		print(c)
		b=c
x=int(input("Enter number"))
fib(x)
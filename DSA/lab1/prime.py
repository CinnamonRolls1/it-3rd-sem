def isprime(n):
	f=0
	for i in range(2,int(n**0.5)+1):
		if(n%i==0):
			print ("Non-prime")
			f=1
			break
	if(f==0):
		print("Prime")
x=int(input("Enter number "))
isprime(x)
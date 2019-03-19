#this code does not work

from Mystack import Stack

#implement precedence 

def infpost(inp):
	S=Stack()
	
	data=inp.split()
	for i in range(0,len(data)):
		if(data[i]=="+" or data[i]=="-" or data[i]=="*" or data[i]=="/"):
			x=S.Pop()
			op=S.Pop()
			y=S.Pop()
			ans=x + ' ' + y + ' ' + op
			S.Push(ans)
		else:
			S.Push(data[i])
	return S.elements[S.top] 

inp=input("Enter infix expression:")
print("Postfix: ",infpost(inp))
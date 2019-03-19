from Mystack import Stack

def prepost(inp):
	S=Stack()
	data=inp.split()
	
	for i in range(len(data)-1,-1,-1):
		if(data[i]=="+" or data[i]=="-" or data[i]=="*" or data[i]=="/"):
			x=S.Pop()
			y=S.Pop()
			ans=x + ' ' + y + ' ' + data[i]
			S.Push(ans)
		else:
			S.Push(data[i])
	
	return S.elements[S.top]

inp=input("Enter prefix expression:")
print("Converted to postfix: ",prepost(inp))
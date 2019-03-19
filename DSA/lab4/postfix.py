from Mystack import Stack

def post(inp):
	S=Stack()
	data=inp.split()
	
	for i in range(0,len(data)):
		if(data[i]=="+" or data[i]=="-" or data[i]=="*" or data[i]=="/" or data[i]=="^"):
			a=S.Pop()
			b=S.Pop()
			if(data[i]=="^"):
				op="**"
			else:
				op=data[i]
			result=b+op+a
			S.Push(str(eval(result)))
		else:
			S.Push(data[i])
	return S.elements[S.top] 

inp=input("Enter postfix expression:")
print("Evaluation: ",post(inp))
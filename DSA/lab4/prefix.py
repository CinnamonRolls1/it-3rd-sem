from Mystack import Stack

def pref(inp):
	S=Stack()
	data=inp.split()
	
	for i in range(len(data)-1,-1,-1):
		
		if(data[i]=="+" or data[i]=="-" or data[i]=="*" or data[i]=="/"):
			a=S.Pop()
			b=S.Pop()
			result=a+data[i]+b
			S.Push(str(eval(result)))
		
		else:
			S.Push(data[i])
	return S.elements[S.top]

inp=input("Enter prefix expression:")
print("Evaluation: ",pref(inp))
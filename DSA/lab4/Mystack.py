class Stack :
	def __init__(self):
		self.elements=[]
		self.top=-1
	def Push(self,x):
		self.top+=1
		self.elements.append(x)
	def isEmpty(self):
		if self.top==-1:
			return True
		return False
	def Pop(self):
		if self.isEmpty():
			print("Stack is already empty")
			return None
		self.top-=1
		return self.elements.pop()


class adjNode:
	def __init__(self,val,nxt=None,colour='white',parent=None,dist=0):
		self.val = val
		self.next = nxt
		self.colour = colour
		self.parent = parent
		self.dist = dist

class adjList:
	def __init__(self,n):
		self.elements=[adjNode(i) for i in range(n)]

	def listChain(self,pair,repeat=0):
		#chains into adjacency list 
		f=0
		node=self.elements[int(pair[0])]
		while node.next!=None:
			if node.val==int(pair[1]):
				f=1
				break
			node=node.next
		if f==0: #flag is used to skip duplicates
			node.next=adjNode(int(pair[1]))
			if repeat==0: #reversed association
				self.listChain(pair[::-1],1)

	def edgeCheck(self,pair,n):
		#checks if the entered edges are valid and in range
		try:
			for val in pair:
				if int(val)>n:
					return False
			if len(pair)>2:
				return False
			return True
		except ValueError:
			return False
	def showlist(self):
		for node in self.elements:
			print(node.val, end = "->")
			while node.next!=None:
				node=node.next
				print(node.val, end = " ")
			print()
	def adjacents(self,node):
		a=[]

		node=self.elements[node.val]
		while node.next!=None:
			node=node.next
			a.append(node)
		return a

class adjMatrix:
	def __init__(self,n):
		self.mat = [[0 for i in range(n)] for i in range(n)]
	def matChain(self,pair):
		self.mat[int(pair[0])][int(pair[1])]=self.mat[int(pair[1])][int(pair[0])]=1
	def showmat(self,n):
		for i in range(n):
			for j in range(n):
				print(self.mat[i][j], end="")
			print()

if __name__=='__main__':
	print("Enter the number of vertices:")
	n = int(input())

	aList = adjList(n)
	aMat = adjMatrix(n)
	print("Enter the edges: [CTRL+C to stop entry]")
	try:
		for i in range(0,int((n*(n-1))/2)):
			k=input()
			if aList.edgeCheck(k,n)==False:
				print("Invalid input")
				exit()
			aList.listChain(k)
			aMat.matChain(k)
	except KeyboardInterrupt:
		print()
	except IndexError:
		print('Invalid input')
	else:
		print("Edge limit reached!")
	print("Adjacency List:")
	aList.showlist()
	print("Adjacency Matrix:")
	aMat.showmat(n)

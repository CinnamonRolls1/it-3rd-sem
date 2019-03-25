from heap import MINHEAP
import copy

class distNode :

	def __init__(self,vertex) :
		self.vertex=vertex
		self.dist=float('inf')
		self.pred=None

class weightEdge :

	def __init__(self,vertex1,vertex2,weight) :

		self.vertex1=vertex1
		self.vertex2=vertex2
		self.weight=weight

class DIRGRAPH :

	def __init__(self) :

		self.V=[]
		self.E=[]
		self.adjacencyList={}


	def inputE(self,n) :

		for i in range(n) :
			a=int(input("Enter 1st vertex "))
			b=int(input("Enter 2nd vertex "))
			w=float(input('Enter weight '))

			edge=weightEdge(a,b,w)

			self.E.append(edge)
			print('')

	def fillV(self) :

		for i in self.E :

			if self.V.count(i.vertex1) == 0 :
				self.V.append(i.vertex1)

			if self.V.count(i.vertex2) == 0 :
				self.V.append(i.vertex2)


	def adjacentMatrix(self) :

		adjMatrix=[]
		for i in range(len(self.V)) :
			adjMatrix.append([0 for i in range(len(self.V))])

		for i in self.V:
			for j in self.V:

				if (i,j) in self.E :

					adjMatrix[i][j]=1
					adjMatrix[j][i]=1

		return adjMatrix

	def findAdjacencyList(self) :

		for i in self.V :

			adjList=[]

			for j in self.E :

				if i == j.vertex1 :
					
					adjList.append((j.vertex2,j.weight))

			self.adjacencyList[i]=adjList


class dijkstra :

	def __init__(self,G,source) :

		self.G=G
		self.source=source

		#G.inputE(10)
		G.fillV()

		G.findAdjacencyList()

		#print(G.V)

		#for i in G.E :
		#	print('(',i.vertex1,',',i.vertex2,') ',i.weight)

		#print('')

		#print(G.adjacencyList)

		self.vertexList=[distNode(i) for i in G.V]
		self.updatedList=[]

	def search(self,key) :

		for i in self.vertexList :

			 if i.vertex == key :
			 	return i

		return None


	def performDijkstra(self):
		
		current=self.search(self.source)

		current.dist=0

		h=MINHEAP()

		h.heapList=self.vertexList

		h.buildHeap()

		while not h.isEmpty() :
			

			w=h.extractMin()
			self.updatedList.append(w)

			for v in G.adjacencyList[w.vertex] :

				#print('v ',v[0])
				vNode=self.search(v[0])
				
				if vNode == None :
					continue

				weight=v[1]

				newDist=w.dist + weight

				if vNode.dist > newDist :
					vNode.dist=newDist
					vNode.pred=w
					h.buildHeap(h.heapList.index(vNode))

	def dispVertex(self) :

		for i in self.updatedList :

			print("vertex: ",i.vertex,'  distance: ',i.dist)
















	#G=DIRGRAPH()

	#G.E=[weightEdge(2,1,3),weightEdge(1,3,6),weightEdge(1,4,3),weightEdge(4,2,1),weightEdge(5,2,4),weightEdge(3,4,2),weightEdge(4,3,1),weightEdge(5,4,2)]

	#G.E=[weightEdge(1,2,5),weightEdge(2,3,3),weightEdge(3,2,2),weightEdge(1,3,10),weightEdge(3,4,1),weightEdge(2,4,9),weightEdge(2,5,2),weightEdge(5,4,4),weightEdge(4,5,6)]


if __name__=='__main__':
	G=DIRGRAPH()
	print("Enter the number of vertices:")
	n = int(input())

	print("Enter v1, v2 and edge weight: [CTRL+C to stop entry]")
	try:
		#for i in range(0,int((n*(n-1))/2)):
		while True:
			print('V1:')
			v1=int(input())
			print('V2:')
			v2=int(input())
			print('Edge weight:')
			e=int(input())
			
			G.E.append(weightEdge(v1,v2,e))
	except KeyboardInterrupt:
		print('Input terminated')
		

	
	test=dijkstra(G,1)
	test.performDijkstra()
	test.dispVertex()










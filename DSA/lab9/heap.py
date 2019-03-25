
class distNode :

	def __init__(self,vertex) :
		self.vertex=vertex
		self.dist=float('inf')


class 	MINHEAP:

	def __init__(self) :

		self.heapList=[]



	def left(self,i):

		return 2*i +1

	def right(self,i) :

		return 2*i +2


	def heapify(self,i) :

		l=self.left(i)
		r=self.right(i)


		smallest=i

		if (l < len(self.heapList) and self.heapList[smallest].dist > self.heapList[l].dist) :
			smallest=l

		if (r < len(self.heapList) and self.heapList[smallest].dist > self.heapList[r].dist) :
			smallest=r


		if smallest != i :

			#print('heapify ',i)

			self.heapList[i],self.heapList[smallest]=self.heapList[smallest],self.heapList[i]
			self.heapify(smallest)


	def buildHeap(self,lim=-1) :

		if lim == -1 :
			lim=len(self.heapList)//2 -1



		for i in range(lim,-1,-1) :

			self.heapify(i)

	def extractMin(self) :

		x=self.heapList[0]

		self.heapList[0],self.heapList[-1]=self.heapList[-1],self.heapList[0]
		self.heapList.pop()

		self.heapify(0)

		return x

	def insert(self,x) :

		self.heapList.append(x)

		print(self.heapList)

		i=len(self.heapList) -1

		#print(self.heapList[i])
		while i > 0 :



			parent=(i-1) // 2

			if self.heapList[i].dist < self.heapList[parent].dist :
				self.heapList[i],self.heapList[parent]=self.heapList[parent],self.heapList[i]

			else :
				break

			i=parent



	def isEmpty(self) :

		if self.heapList == [] :
			return True

		else :
			return False



def main() :

	h=MINHEAP()

	h.heapList=[23,32,12,345,22,1,76,56]

	h.buildHeap()

	print(h.heapList)

	h.heapList[4]=10

	h.buildHeap(4)

	print(h.heapList)

	print(h.extractMin())

	print(h.heapList)

	h.insert(11)

	print(h.heapList)



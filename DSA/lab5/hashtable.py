#incomplete
import llr
table = [None for i in range(30)]

def tabinsert(item, tab):
	sum=0
	for ch in item:
		sum+=ord(ch)
	loc=sum%30
	if tab[loc] == None:
		tab[loc]=item
	else:
		chain(item, loc)

def chain(item, loc, tab):
	tab[loc]=LinkedList()
	tab[loc].insert(loc, item)


def tabsearch(val):
	pos=None
	for it in table:
		if type(it)==LinkedList():
			pos=it.search(val)
		else:
			if it==val:
				pos
	pass

def keys():
	pass
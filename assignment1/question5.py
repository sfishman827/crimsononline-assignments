from pprint import pprint

class HashableList(list):
	def __hash__(self):
		return hash(tuple(self[i] for i in range(0, len(self))))
		
#==TEST CODE==

arr = HashableList([1, 2, 3])
it = {}
it[arr] = 7
it[HashableList([1, 5])] = 3

print "it[HashableList([1, 5])] => ",
pprint(it[HashableList([1, 5])])

print "it[HashableList([1, 2, 3])] => ",
pprint(it[HashableList([1, 2, 3])])
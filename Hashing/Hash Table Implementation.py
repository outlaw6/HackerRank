class HashTable:
    def __init__(self):
    	self.size = 11
    	self.slot = [None] * self.size
    	self.data = [None] * self.size

    
    def put(self, key, data):
    	
    	hashvalue = self.hash(key, self.size)

    	if self.slot[hashvalue] == None:
    		self.slots[hashvalue] = key
    		self.data[hashvalue]  = data

    	else:
    		if self.slots[hashvalue] == key:
    			self.data[hashvalue] = data # replace values

    		else:
    			nextslot = self.rehash(hashvalue, self.size)

    			while self.slots[nextslot] != None and self.slots[hashvalue] != key:
    				nextslot = self.rehash(nextslot, self.size)

    			if self.slots[nextslot] == None:
    				self.slots[nextslot] = key
    				self.data[hashvalue] = data
    			else:
    				self.data[nextslot] = data

    def hash(self, key, size):
    	return key % size
    def rehash(self, oldhash, size):
    	return (oldhash+1) % size

if __name__ == '__main__':
	print()
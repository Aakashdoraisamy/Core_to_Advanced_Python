class Hashmap:
    
    def __init__(self,size = 10):
        self.size = 10
        self.hashlist = [None]*self.size
        
    def getindex(self,key):
        return hash(key)%self.size
        
    def __setitem__(self,key,value):
        index = self.getindex(key)
            
        if self.hashlist[index] is None:
            self.hashlist[index] = [[key,value]]
        else:
            self.hashlist[index].append([key,value])
    
    def __getitem__(self,key):
        index = self.getindex(key)
        
        if self.hashlist[index]:
            sublist = self.hashlist[index]
            for pairs in sublist:
                if pairs[0] == key:
                    return pairs[1]
        
        return 'Key Not Found'
        
dict = Hashmap()
dict['name'] = 'Human'
dict['age'] = 0
print(dict.hashlist)
print(dict['name'])

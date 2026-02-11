class RandomizedSet:

    def __init__(self):
        self.randlist = []
        self.randdict = {}

    def insert(self, val: int) -> bool:
        if val in self.randdict:
            return False 

        self.randdict[val] = len(self.randlist)
        self.randlist.append(val)
        return True 

    def remove(self, val: int) -> bool:
        if val not in self.randdict:
            return False 
        
        todel = self.randdict[val]
        toswap = self.randlist[-1]

        self.randlist[todel] = toswap
        self.randdict[toswap] = todel
        
        self.randlist.pop()
        del self.randdict[val]
        
        return True
    def getRandom(self) -> int:
        return random.choice(self.randlist)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
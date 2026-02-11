class FrequencyTracker:

    def __init__(self):
        self.hash_map = defaultdict(int)
        self.freqhashmap = defaultdict(int)

    def add(self, number: int) -> None:
        old_freq = self.hash_map[number]
        if old_freq > 0:
            self.freqhashmap[old_freq] -= 1
        
        self.hash_map[number] += 1
        new_freq = self.hash_map[number]
        self.freqhashmap[new_freq] += 1

    def deleteOne(self, number: int) -> None:
        old_freq = self.hash_map[number]
        if old_freq == 0:
            return
        self.hash_map[number] -= 1
        self.freqhashmap[old_freq] -= 1
        new_freq = self.hash_map[number]

        if new_freq > 0:
            self.freqhashmap[new_freq] += 1

        

    def hasFrequency(self, frequency: int) -> bool:
        return self.freqhashmap[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
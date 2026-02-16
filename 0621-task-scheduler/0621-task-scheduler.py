class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_freq = max(count.values())
        value_with_max_freq = sum(max_freq == x for x in count.values())
        
        return max(len(tasks), ((max_freq-1 )* (n+1 )+ value_with_max_freq))
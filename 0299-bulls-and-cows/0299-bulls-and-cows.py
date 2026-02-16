class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count_1 = defaultdict(int)
        count_2 = defaultdict(int)

        count_bull , count_cow  = 0 ,0
        for i ,j in zip(secret,guess):
            if i == j :
                count_bull += 1
            else:
                count_1[i] += 1
                count_2[j] += 1
        
        count_cow = sum(min(count_1[c],count_2[c]) for c in count_1 )
        
        return f"{count_bull}A{count_cow}B"
                       
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for key , freq in count.items():
            check_1 = key + 1
            check_2 = math.ceil(freq / check_1)
            ans += check_1 * check_2 
        return ans 
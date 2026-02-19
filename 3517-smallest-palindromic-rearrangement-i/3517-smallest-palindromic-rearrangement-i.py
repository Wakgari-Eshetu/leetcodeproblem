class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        result , middle  = [] , ""
        for char in sorted(count.keys()):
            if count[char] % 2 == 1:
                middle = char
            result.append(char*(count[char]//2))
        ans = ''.join(result)

        return ans + middle + ans[::-1]

        
        
        

        
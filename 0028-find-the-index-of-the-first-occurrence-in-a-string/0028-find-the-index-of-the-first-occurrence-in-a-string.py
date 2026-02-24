class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left , right = 0 , len(needle)-1

        left1 , right1 = 0 , len(haystack)

        while right <= right1:
            if haystack[left:right+1] == needle:
                return left
            left = right + 1
            right = right + len(needle)
        
        return -1 

        

       
        
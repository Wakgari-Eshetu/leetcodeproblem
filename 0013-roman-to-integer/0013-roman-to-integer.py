class Solution:
    def romanToInt(self, s: str) -> int:
        ans  = 0
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D": 500 ,"M":1000 }
        lis = ["IV","IX","XL","XC","CD","CM"]
        
        for char in s:
            ans += dic[char]
        
        if "IV" in s or "IX" in s:
            ans -= 2
        if "XL" in s or "XC" in s:
            ans -= 20
        if "CD" in s or "CM" in s:
            ans -= 200

        
        return ans 

        
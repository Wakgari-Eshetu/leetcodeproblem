class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        while n!=1 and n not in check:
            check.add(n)
            sum = 0
            while n>0:
                res = n%10
                sum+=res*res
                n=n//10
            n = sum
        if n==1:
            return True
        else:
            return False



        
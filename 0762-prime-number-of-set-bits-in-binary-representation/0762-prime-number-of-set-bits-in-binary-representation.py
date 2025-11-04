class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        def isprime(n)->bool:
            if n == 1 or n==0:
                return False 
            if n== 2 or n==3:
                return True
            for i in range(2,n):
                if n%i==0:
                    return False 
            return True

        total = 0
        for i in range(left,right+1):
            count = 0
            v = list(bin(i)[2:])
            for j in v:
                if j =='1':
                    count+=1
            if isprime(count):
                total+=1
        return total
        
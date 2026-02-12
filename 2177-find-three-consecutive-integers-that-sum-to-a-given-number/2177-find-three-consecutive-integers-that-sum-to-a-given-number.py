class Solution(object):
    def sumOfThree(self, num):
        if num % 3 == 0:
            value = num/3
            return [ value-1, value , value +1]
        else:
            return []
        
        
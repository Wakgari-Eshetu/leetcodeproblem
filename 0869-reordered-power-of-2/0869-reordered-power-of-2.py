class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def check_num(num):
            result_check = [0]*10
            while num > 0:
                num , rem = divmod(num , 10)
                result_check[rem] += 1
            return result_check 
        
        ans_check = check_num(n)
        power_two = 1
        while power_two <= pow(10,9):
            if check_num(power_two) == ans_check:
                return True 
            power_two = power_two * 2
        return False 



        
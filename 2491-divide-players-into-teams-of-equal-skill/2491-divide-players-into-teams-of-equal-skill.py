class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left , right = 0 , len(skill)-1
        result , result_sum = 0,[]
        while left < right:
            result_sum.append(skill[left] + skill[right])
            result += skill[left]*skill[right]
            left += 1
            right -= 1
        
        if len(set(result_sum)) == 1:
            return result

        else:
            return -1 
        
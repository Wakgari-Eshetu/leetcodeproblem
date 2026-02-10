class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        diclist1 = {name: index for index ,name in  enumerate(list1)}
        min_sum = float("inf")
        result = []

        for j , name in  enumerate(list2):
            if name in diclist1:
                i = diclist1[name]
                curr_sum = i+j

                if curr_sum < min_sum:
                    min_sum = curr_sum
                    result = [name] 
                elif curr_sum == min_sum:
                    result.append(name)

        return result 



        
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        result = []
        check = []
        for num in arr1:
            if num not in arr2:
                check.append(num)
        check=sorted(check)
        for num in arr2:
            result += [num]*count[num]
            count.pop(num)
        

        return result + check

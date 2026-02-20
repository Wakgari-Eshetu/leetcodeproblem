class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dicts = {value : index for index , value in enumerate(order)}
        custom_sort = sorted(s , key= lambda value : dicts.get(value, 0 ))
        return ''.join(custom_sort)  
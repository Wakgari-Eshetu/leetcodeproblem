class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextgreater = defaultdict(lambda:-1)

        for num in nums2:
            while stack and stack[-1] < num:
                nextgreater[stack.pop()] = num
            stack.append(num)
        
        return [nextgreater[num] for num in num1]
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum  = []
        curr_sum = 0
        for num in nums:
            curr_sum += num 
            self.prefix_sum.append(curr_sum)
        

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix_sum[right]
        left_sum = self.prefix_sum[left - 1] if left > 0 else 0

        return right_sum - left_sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
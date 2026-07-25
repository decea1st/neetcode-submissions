class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]
        accProd = 1 # accumulates product so far
        for i in range(len(nums)):
            result[i] = accProd
            accProd *= nums[i]
        accProd = 1 # reset
        for j in range(len(nums)-1, -1, -1):
            result[j] *= accProd
            accProd *= nums[j]
        return result
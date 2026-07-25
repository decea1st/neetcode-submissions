class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = math.prod(nums)
        for i in range(len(nums)):
            if nums[i] != 0: result.append((product // nums[i]))
            else:
                nums[i] = 1
                result.append((math.prod(nums) // nums[i]))
                nums[i] = 0
        return result
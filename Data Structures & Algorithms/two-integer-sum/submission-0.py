class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNums = {}
        index1, index2 = 0, 0

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashNums:
                index1 = hashNums[comp]
                index2 = i
            hashNums[nums[i]] = i

        if index1 > index2:
            return [index2, index1]
        else:
            return [index1, index2]
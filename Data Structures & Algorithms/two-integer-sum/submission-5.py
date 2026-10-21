class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in hashMap:
                return [min(hashMap[comp], i), max(hashMap[comp], i)]
            hashMap[n] = i
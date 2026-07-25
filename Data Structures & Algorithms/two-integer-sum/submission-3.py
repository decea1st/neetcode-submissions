class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashN = {}

        for n in range(len(nums)):
            comp = target - nums[n]
            
            if comp in hashN:
                if hashN.get(comp) < n: return [hashN.get(comp),n]
                else: return [n,hashN.get(comp)]

            hashN[nums[n]] = n
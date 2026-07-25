class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashX = {}
        result = []

        for x in nums:
            hashX[x] = hashX.get(x, 0) + 1
        
        while len(hashX) > k:
            hashX.pop(min(hashX, key=hashX.get))

        for n in hashX:
            result.append(n)

        return (result)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashX = {}
        result = []

        for x in nums:
            hashX[x] = hashX.get(x, 0) + 1
        
        hashS = sorted(hashX, key=hashX.get, reverse=True)

        return (hashS[:k])
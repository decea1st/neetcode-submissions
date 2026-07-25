class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreqs = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []

        for num, freq in numFreqs.items():
            buckets[freq].append(num)

        for bucket in reversed(buckets):
            result.extend(bucket)
            if len(result) >= k: return (result)
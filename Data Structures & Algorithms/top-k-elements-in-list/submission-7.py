class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = Counter(nums)
        topK    = numFreq.most_common(k)
        result  = [x for x, _ in topK]
        return  result
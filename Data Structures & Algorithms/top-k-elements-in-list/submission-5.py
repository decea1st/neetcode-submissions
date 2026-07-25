class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashX = Counter(nums)
        numbers = [[] for _ in range(len(nums) + 1)]
        result = []

        for key, freq in hashX.items():
            numbers[freq].append(key)

        length = 0
        for n in range(len(numbers)-1, -1, -1):
            if numbers[n] == []: pass
            else:
                result.append(numbers[n])
                length += len((numbers[n]))
            if length >= k: break
        
        return (list(chain.from_iterable(result)))
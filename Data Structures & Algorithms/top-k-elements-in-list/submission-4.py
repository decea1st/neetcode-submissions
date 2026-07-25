class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashX = Counter(nums)
        numbers = [[None] for _ in range(len(nums) + 1)]
        result = []

        for key in hashX:
            if numbers[hashX[key]] == [None]:
                numbers[hashX[key]] = [key]
            else:
                numbers[hashX[key]].append(key)

        iterator = 0
        length = 0
        for n in range(len(numbers)-1, -1, -1):
            if numbers[n] == [None]: pass
            else:
                result.append(numbers[n])
                iterator += 1
                length += len((numbers[n]))
            if iterator == k or length >= k: break
        
        return (list(chain.from_iterable(result)))
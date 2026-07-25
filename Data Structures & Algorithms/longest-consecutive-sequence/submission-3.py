class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(set(nums)) == 1: return 1

        sortedNums = sorted(list(set(nums)))
        minNum = min(sortedNums)
        currCount = 1
        maxCount = float('-inf')
        lastNum = minNum

        print(sortedNums)
        for i in range(1, len(sortedNums)):
            currNum = sortedNums[i]
            if currNum == lastNum+1:
                currCount += 1
                lastNum = currNum
                maxCount = max(currCount, maxCount)
            else:
                lastNum = currNum
                currCount = 1

        return maxCount
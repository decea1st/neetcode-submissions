class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end, start = len(nums)-1, 0
        while start <= end:
            mid = (start + end) // 2
            curr = nums[mid]
            if curr == target: return mid
            if curr > target: end = mid-1
            if curr < target: start = mid+1
        return -1
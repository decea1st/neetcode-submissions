class Solution:
    def binarySearch(self, array, L, R, target):
        while L <= R:
            mid = (L+R)//2
            if array[mid] == target: return mid
            if array[mid] > target: R = mid-1
            if array[mid] < target: L = mid+1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        L, R = 0, n-1

        if target >= nums[L] and target <= nums[(L+R)//2]:
            return self.binarySearch(nums, L, (L+R)//2, target)

        while L <= R:
            mid = (L+R)//2
            if nums[mid] >= nums[0]: L = mid+1
            if nums[mid]  < nums[0]: R = mid-1

        seg2 = L % n
        if target >= nums[seg2] and target <= nums[n-1]:
            return self.binarySearch(nums, seg2, n-1, target)
        if target >= nums[0] and target <= nums[seg2-1]:
            return self.binarySearch(nums, 0, seg2-1, target)
        else:
            return -1
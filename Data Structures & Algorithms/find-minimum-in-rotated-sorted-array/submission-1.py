class Solution:
    def findMin(self, nums: List[int]) -> int:
        # I think position of the min has something to do with how many times the array has been rotated
        # Rotated n times means minumum is in index n. More specifically, min is in n mod len(nums).
        # len(nums) is known, n is not known. How can we find out n in logn time?
        # We can find out how much of the list is sorted using binary search.
        # Start at the middle, go to the right, if less,
            # everything from there to the end is sorted... How can I use this info?
            # Should I go to the unsorted portion and do binary search till I find the sorted and unsorted halves?
            # [ 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20, 1, 2, 3, 4]
            #                              9,            14,      17,
                # After doing 3 rounds of the binary search I know:
                    # Index  0 - 14 is sorted
                    # Index 17 - 19 is sorted
                # The question for my algorithm: Where do I move my pointers when I find an unsorted number?
                # If the goal is make sure R pointer is at the sorted border, then move R to mid-1
                # Morever, moving L doesn't make sense because I already know curr index to end is sorted.
                # I'm leaning towards a while loop with the condition being L <= R,
                    # Move L to mid+1 when curr element > prev, else Move R to mid-1 


        # If it's rotated between 1 and n times, can I just guess what the n is using binary search?
            # L, R = 1, len(nums) - let's say len(nums) is 20
            # L, R = 1, 20
            # Minumum is at index n mod len(nums) -> n mod 20
            # [ 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20, 1, 2, 3, 4]
            # I don't have a "target" so I can't decide whether to move Left or Right.
        n = len(nums)
        L, R, prev = 0, n-1, nums[0]

        while L <= R:
            mid = (L+R) // 2
            if nums[mid] >= prev:
                prev = nums[mid]
                L = mid+1
            elif nums[mid] < prev:
                R = mid-1
        return nums[L % n]
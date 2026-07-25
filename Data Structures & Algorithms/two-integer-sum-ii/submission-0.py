class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashN = {}
        
        for i, n in enumerate(numbers):
            hashN[n] = i

        for i, n in enumerate(numbers):
            complement = target - n
            if complement in hashN and hashN[complement] != i:
                if n < complement:
                    index1 = i
                    index2 = hashN[complement]
                else:
                    index1 = hashN[complement]
                    index2 = i
        print(hashN)
        return [index1+1, index2+1]
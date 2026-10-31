import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = len(position)
        position, speed = zip(*(sorted(zip(position, speed), reverse=True))) 
        time = []

        for i, p in enumerate(position):
            time.append((target-p) / speed[i])

        for i, p in enumerate(position):
            if i < len(position) - 1 and time[i] >= time[i+1]:
                res -= 1
                time[i+1] = time[i]
        return res
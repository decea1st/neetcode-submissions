class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(key=lambda pairs: pairs[0], reverse=True)
        endTimes = []
        fleets = len(position)
        for p, s in pairs:
            endTimes.append((target-p)/s)
        t, i = 0, 1
        while t < len(endTimes)-1:
            while i < len(endTimes) and endTimes[t] >= endTimes[i]:
                fleets -= 1
                i += 1
            t = i
            i = t+1
        return fleets
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(key=lambda pairs: pairs[0], reverse=True)
        endTimes = []
        fleets = len(position)
        # [(10,2),(8,4),(5,1),(3,3),(0,1)]
        # [(10,2),(5,1),(3,3),(0,1)]
        # [1, -1, 7, 3, 12]
        for p, s in pairs:
            endTimes.append((target-p)/s)
        t, i = 0, 1
        print(endTimes)
        while t < len(endTimes)-1:
            print(t+i < len(endTimes))
            print(t)
            while i < len(endTimes) and endTimes[t] >= endTimes[i]:
                fleets -= 1
                i += 1
            t = i
            i = t+1
        return fleets
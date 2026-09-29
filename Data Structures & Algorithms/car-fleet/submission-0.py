class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        pair = [[p,s] for p, s in zip(position, speed)]

        pair.sort()

        for p, s in reversed(pair):
            time_to_target = (target - p) / s
            if len(res) > 0 and time_to_target > res[-1]:
                res.append(time_to_target)
            elif len(res) == 0:
                res.append(time_to_target)

        
        return len(res)

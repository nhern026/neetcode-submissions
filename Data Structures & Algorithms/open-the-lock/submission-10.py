# Session 2, attempt 1: just looking at string building for this

    # i could check target and return distance + 1 when adding neighbhors

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:        
        visited = set()
        q = deque()
        origin = "0000"

        q.append(origin)

        for de in deadends:
            visited.add(de)

        if origin in visited:
            return -1
        else:
            visited.add(origin)



        def addNeighbors(curr):
            for i in range(4): #or len(curr))
                for turn_direction in [-1, 1]:
                    modified_wheel = (int(curr[i]) + turn_direction) % 10
                    new_str = curr[:i] + str(modified_wheel)  + curr[i+1:]

                    if new_str not in visited:
                        q.append(new_str)
                        visited.add(new_str)

        distance = 0
        while q: 
            q_len = len(q)
            for _ in range(q_len):
                curr = q.popleft()
                if curr == target:
                    return distance
                addNeighbors(curr)
            distance+=1 

        return -1


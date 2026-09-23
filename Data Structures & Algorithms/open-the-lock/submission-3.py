# Session 1, attempt 1: got the algo pretty quick, took forever to implement because of type issues.
    # i wanted to use tuples beecause i thought they gave me the inputs as list not as string!
    # terrible showing in that regard. but got the theory down fast so that's good!
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque()
        origin = (0,0,0,0)
        q.append(origin)

        visited = set()
        visited.add(origin)

        list_target = []
        for ltr in target:
            list_target.append(int(ltr))
        tuple_target = tuple(list_target)

        for de in deadends:
            combo_list = []
            for ltr in de:
                combo_list.append(int(ltr))

            tuple_combo_list = tuple(combo_list)
            if origin == tuple_combo_list:
                return -1
            visited.add(tuple_combo_list)

        def addIt(coordsList): # add it to q and visited if not already visited
            tupled_list = tuple(coordsList)
            # print(tupled_list)
            if not (tupled_list in visited): # save time 
                q.append(tupled_list)
                visited.add(tupled_list)

        def addNeighbors(node): # we want to be able to wrap around because we want fastest
            # find possible neighbors while checking for wrap around
                # add them using helper funciton
            coordsList = list(node)
            
            for idx in range(4):
                # add pos neighbor
                if coordsList[idx] == 9: 
                    coordsList[idx] = 0
                    addIt(coordsList) # add it
                    coordsList[idx] = 9
                else:
                    coordsList[idx] += 1
                    addIt(coordsList) # add it
                    coordsList[idx] -= 1
                
                # add neg neighbor
                if coordsList[idx] == 0:
                    coordsList[idx] = 9
                    addIt(coordsList) # add it
                    coordsList[idx] = 0
                else:
                    coordsList[idx] -= 1
                    addIt(coordsList) # add it
                    coordsList[idx] += 1

        turns = 0
        while q: 
            # print(len(visited))
            q_len = len(q)
            for _ in range(q_len):
                curr = q.popleft()
                if curr == tuple_target:
                    return turns
                
                addNeighbors(curr) # adding to q and visited
            
            turns += 1
        
        return -1

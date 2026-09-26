# Session 2, attempt 1: Kahn's Algo
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque()
        pre2crs = defaultdict(list) # prereq mapping
        incoming_degrees = [0] * numCourses


        # build depedency map
        for crs, pre in prerequisites:
            pre2crs[pre].append(crs)
            incoming_degrees[crs] += 1

        # add initial courses with no prereqs
        for i, degree in enumerate(incoming_degrees):
            if degree == 0:
                q.append(i)


        res = []
        while q: 
            curr = q.popleft()
            res.append(curr)

            for post_course in pre2crs[curr]:
                incoming_degrees[post_course] -= 1
                if incoming_degrees[post_course] == 0:
                    q.append(post_course)
        
        return res if len(res) == numCourses else []
            


        

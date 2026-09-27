# Session 1, attempt 1: 
# this version i think is         

# time O(w*w*m + (w+e)) = O(w*w*m + ).    w = len(wordList), m = len(word1)
# time O(w*w*m) because of the map, every word can connect to every word and each word is m long


# make adjacency list/map
# perform bfs from origin node
# traverse graph until you find endWord or until no other edges can traversed 
    # when you find target, return the path 

# return 0 when endWord not in wordList and also when not possible to reach

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: # we have to do set here b
            return 0
        
        def one_letter_difference(word1, word2):
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
                    if diff > 1:
                        return False

            return True if diff == 1 else False # it can either be 1 or 0 here

        edge_map = defaultdict(list)

        # O(w*w*m) w = len(wordList), m = len(word1)
        for i in range(len(wordList)): 
            if one_letter_difference(wordList[i], beginWord):
                edge_map[beginWord].append(wordList[i])
            for j in range(i, len(wordList)): 
                if one_letter_difference(wordList[i], wordList[j]):
                    edge_map[wordList[i]].append(wordList[j])
                    edge_map[wordList[j]].append(wordList[i])
           
        q = deque()
        q.append(beginWord)

        path = 1
        visited = set()
        visited.add(beginWord)
        while q: 
            q_len = len(q)

            for _ in range(q_len): # loop through level
                curr = q.popleft()
                if curr == endWord:
                    return path
                
                for word in edge_map[curr]:
                    if word not in visited:
                        visited.add(word)
                        q.append(word)
            
            path += 1
        
        return 0


# Session 1, attempt 2: optimal version
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # build edge map
        if endWord not in wordList:
            return 0 

        pattern2words = defaultdict(list) # pattern : [word1, word2, ...]
        for word in wordList: 
            for i, ltr in enumerate(word):
                pattern = word[:i] + "*" + word[i+1:]
                pattern2words[pattern].append(word)

        # bfs
        q = deque()
        q.append(beginWord)
        path = 1
        while q: 
            q_len = len(q)
            for _ in range(q_len):
                curr = q.popleft()
                if curr == endWord:
                    return path
                
                #traverse all patterns
                for idx, ltr in enumerate(curr):
                    pattern = curr[:idx] + "*" + curr[idx+1:]
                    if pattern in pattern2words:
                        for word in pattern2words[pattern]:
                            q.append(word)
                        pattern2words[pattern] = []
            path += 1

        return 0 
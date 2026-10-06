# Session 1, attempt 1: as part of claude's mock
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        edge_list = defaultdict(list) # 'ltr' : ['ltr1', 'ltr2'] # that come after it
        # what comes before : what comes after    
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            
            word_len = min(len(word1), len(word2))
            
            changed = False
            for ltr_idx in range(word_len):
                if not changed and word1[ltr_idx] != word2[ltr_idx]:
                    edge_list[word1[ltr_idx]].append(word2[ltr_idx])
                    changed = True
                    break
                    
            if not changed and len(word2) < len(word1):
                return ""
        
        ltr_set = set()
        for word in words:
            for ltr in word:
                ltr_set.add(ltr)
        
        res = []
        visited = set()
        cycle = set()
        def dfs(ltr):
            if ltr in cycle:
                return False
            if ltr in visited:
                return True
            
            cycle.add(ltr)
            for nxt_ltrs in edge_list[ltr]:
                if not dfs(nxt_ltrs):
                    return False
            
            cycle.remove(ltr)
            res.append(ltr)
            visited.add(ltr)
            return True
        
        
        
        # when we loop through each letter, if false return ""
        # if not and all good, then return reversed(res)
        while ltr_set:
            ltr = ltr_set.pop()
            if not dfs(ltr):
                return ""
        
        return "".join(reversed(res))
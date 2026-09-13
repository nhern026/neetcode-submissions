from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #holy smokes. 
        s_ltrCount = Counter(s)
        t_ltrCount = Counter(t)
        return s_ltrCount == t_ltrCount

        #counter!
        # you can add them

        # c1 = Counter(a=3, b=1)
        # c2 = Counter(a=1, b=2)
        # print(c1 + c2)  # Addition: Counter({'a': 4, 'b': 3})
        # print(c1 - c2)  # Subtraction (keeps positive results): Counter({'a': 2})
        # print(c1 & c2)  # Intersection (min of counts): Counter({'a': 1, 'b': 1})
        # print(c1 | c2)  # Union (max of counts): Counter({'a': 3, 'b': 2})


        #you can print out most common!
        # print(word_counts.most_common(2)) 
        #Output: [('apple', 3), ('banana', 2)]
        #this uses heaps and timsort for speedy klogk big O.


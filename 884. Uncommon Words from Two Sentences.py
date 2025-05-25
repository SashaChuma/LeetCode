import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
from queue import Queue
import math
import itertools
import heapq
from collections import Counter
import numpy 
import pprint
# Definition for singly-linked list.
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1 = Counter(s1.split(' '))
        c2 = Counter(s2.split(' '))
        return list(w1 for w1 in c1 if c1[w1] == 1 and w1 not in c2)\
        +list(w2 for w2 in c2 if c2[w2] == 1 and w2 not in c1)
start_time = time.time()
t = Solution()
root = t.uncommonFromSentences("this apple is sweet", "this apple is sour")

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

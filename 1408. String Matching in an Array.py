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
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key=len, reverse=True)
        res = []
        s = words[0]
        for w in words[1:]:
            if w in s:
                res.append(w)
            else: 
                s += f" {w}" 
        return res 
start_time = time.time()
t = Solution()
root = t.stringMatching(["mass","as","hero","superhero"])

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

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

class Solution:
    def removeDuplicates(self, s: str) -> str:
        letters = defaultdict(list)
        for i in range(len(s)):
            letters[s[i]].append(i)
        stack = []
        for i in range(len(s)):
            l = s[i]
            if any(l == c[0] for c in stack):
                continue
            while stack and stack[-1][0] > l and stack[-1][1]>i:
                stack.pop()
            stack.append((l, letters[l][-1])) 
        return "".join(c[0] for c in stack)
start_time = time.time()
t = Solution()
root = t.removeDuplicates("bbcaac")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

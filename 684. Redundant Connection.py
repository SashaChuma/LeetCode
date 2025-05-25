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
from collections import deque 
import numpy 
import pprint
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(i):
            if parent[i] == i:
                return i
            return find(parent[i])
        def unite(i, j):
            irep = find(i)
            jrep = find(j)
            parent[irep] = jrep
        
        parent = list(range(len(edges)))
        for e in edges:
            f1 = find(e[0]-1)
            f2 = find(e[1]-1)
            if f1 == f2:
                return e
            parent[f1] = f2
        return []
start_time = time.time()
t = Solution()
root = t.findRedundantConnection([[1,2],[1,3],[2,3]])
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

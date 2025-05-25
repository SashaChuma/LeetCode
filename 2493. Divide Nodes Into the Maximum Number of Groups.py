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
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        def check(v):
            colors = defaultdict(int)
            visited = set()
            visited.add(v)
            colors[v] = 0
            d = deque([v])
            depth = 0
            while d:
                v1 = d.popleft()
                for v2 in g[v1]:
                    if v2 not in visited:
                        visited.add(v2)
                        colors[v2] = colors[v1]+1
                        depth = colors[v2]
                        d.append(v2)
                    else:
                        if colors[v2]%2 == colors[v1]%2:
                            return (-1, False, [])
            return (depth+1, True, colors)
            
        def find(i):
            if parent[i] == i:
                return i
            return find(parent[i])
        def unite(i, j):
            irep = find(i)
            jrep = find(j)
            parent[irep] = jrep
        
        g = [[] for _ in range(n)]
        parent = list(range(n))
        color = -1*len(edges)
        for e in edges:
            g[e[0]-1].append(e[1]-1)
            g[e[1]-1].append(e[0]-1)

            f1 = find(e[0]-1)
            f2 = find(e[1]-1)
            parent[f1] = f2
        forest = defaultdict(set)
        for v in range(n):
            p = find(v)
            forest[p].add(v)
        result = 0
        for r in forest.keys():
            max_depth, valid, levels = check(r)
            if not(valid):
                return -1
            leaves = [k for v, k in enumerate(levels) if v >= max_depth-1]
            for v in leaves:
                d, _, _ = check(v)
                max_depth = max(max_depth, d)
            result += max_depth
        return result 
start_time = time.time()
t = Solution()
root = t.magnificentSets(92, [[67,29],[13,29],[77,29],[36,29],[82,29],[54,29],[57,29],[53,29],[68,29],[26,29],[21,29],[46,29],[41,29],[45,29],[56,29],[88,29],[2,29],[7,29],[5,29],[16,29],[37,29],[50,29],[79,29],[91,29],[48,29],[87,29],[25,29],[80,29],[71,29],[9,29],[78,29],[33,29],[4,29],[44,29],[72,29],[65,29],[61,29]])
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

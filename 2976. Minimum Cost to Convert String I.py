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
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def calc_letter(l):
            result = dict()
            vertex = {l:0}
            visited = set()
            while len(vertex) > 0:
                p,v = min((v,k) for k,v in vertex.items())
                visited.add(v)
                result[v] = p 
                del(vertex[v]) 
                for v2,p2 in edges[v].items():
                    if v2 in visited:
                        continue
                    if v2 not in vertex or p+p2<vertex[v2]:
                        vertex[v2] = p+p2
                
            return result
        n = len(source)
        if source == target:
            return 0
        edges = defaultdict(dict)
        letter_path = {}
        result = 0
        for l1, l2, c in zip(original, changed, cost):
            if l1 == l2:
                continue
            if l2 not in edges[l1] or edges[l1][l2] > c:
                edges[l1][l2] = c
        for ch1, ch2 in zip(source, target):
            if ch1 == ch2: 
                continue
            if ch1 not in letter_path:
                letter_path[ch1] = calc_letter(ch1)
            if ch2 not in letter_path[ch1]:
                return -1
            result += letter_path[ch1][ch2]
        return result
        
start_time = time.time()
t = Solution()
root = t.minimumCost("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

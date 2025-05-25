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
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [arr[0]]
        for i in range(1, len(arr)):
            prefix.append(prefix[-1]^arr[i])
        result = []
        for q in queries:
            r = prefix[q[1]]
            l = prefix[q[0]-1] if q[0] > 0 else 0
            result.append(l^r)
        return result 
start_time = time.time()
t = Solution()
root = t.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]])

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

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
import bisect
def print_m(m):
    for r in m:
        print(" ".join(f"{num:4d}" for num in r))
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        p = [0]*n
        m_result = 0
        m_val = 0
        for i in range(n):
            m_val = max(p[i], m_val)
            val = m_val + questions[i][0]
            next = i + questions[i][1] + 1
            if next < n:
                p[next] = max(p[next], val)
            if val > m_result: 
                m_result = val
        return m_result
start_time = time.time()
t = Solution()
root = t.mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]])

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

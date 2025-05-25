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
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suff = [nums[-1]]*n
        pref = [nums[0]]*n
        m_pref = [0]*n
        for i in range(n-2, -1, -1):
            suff[i] = max(suff[i+1], nums[i])
        for i in range(1, n):
            pref[i] = max(pref[i-1], nums[i])
            m_pref[i] = max(m_pref[i-1], pref[i]-nums[i])
        
        #print(suff)
        #print(pref)
        #print(m_pref)
        val = max(m_pref[i]*suff[i+1] for i in range(n-1))
        if val < 0:
            val = 0
        return val
start_time = time.time()
t = Solution()
root = t.maximumTripletValue([1,10,3,4,19])

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

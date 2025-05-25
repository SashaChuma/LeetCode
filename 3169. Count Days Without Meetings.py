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
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        d = 1
        result = 0
        for m in meetings:
            if d < m[0]:
                result += m[0]-d
            if m[1] >= d:
                d = m[1]+1
        if d <= days: 
            result += days-d+1
        return result 
start_time = time.time()
t = Solution()
root = t.countDays(5, [[2,4],[1,3]])

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

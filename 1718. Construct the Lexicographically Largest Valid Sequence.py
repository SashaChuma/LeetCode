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

class Solution:
    
    def constructDistancedSequence(self, n: int) -> List[int]:
        def process(step) -> bool:
            if step == n:
                matched.append(list(result))
                return True
            pos = 0 
            for i in range(2*n-1):
                if result[i] == 0:
                    pos = i
                    break    
            for x in range(n, 1, -1):
                if visited[x] == 0 and pos+x < 2*n-1 and result[pos+x] == 0:
                    visited[x] = 1
                    result[pos] = x
                    result[pos+x] = x
                    if process(step+1):
                        return True
                    result[pos] = 0
                    result[pos+x] = 0
                    visited[x] = 0
            if visited[1] == 0:
                visited[1] = 1
                result[pos] = 1
                if process(step+1):
                    return True
                result[pos] = 0
                visited[1] = 0
            return False
        matched = []
        visited = [0 for i in range(n+1)]
        result = [0 for i in range(2*n-1)]
        process(0)
        return matched[0]
start_time = time.time()
t = Solution()
root = t.constructDistancedSequence(5)

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

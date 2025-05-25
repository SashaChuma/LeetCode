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
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = (m+n)*mean
        n_sum = total-sum(rolls)
        if n_sum > n*6 or n_sum < n:
            return []
        n6 = (n_sum-n)//5
        conn = (n_sum-n)%5
        if conn > 0:
            return [6]*n6 + [conn+1] + [1]*(n_sum-n6*6-conn-1)
        else: 
            return  [6]*n6 + [1]*(n_sum-n6*6)
        
start_time = time.time()
t = Solution()
root = t.missingRolls([1,5,6], 3, 4)
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

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
    def canConstruct(self, s: str, k: int) -> bool:
        dic = Counter(s)
        if k > len(s):
            return False
        odd = [v for v in dic.values() if v % 2 == 1]
        even= [v/2 for v in dic.values() if v % 2 == 0 or v > 2]
        if len(odd) > k: 
            return False
        k -= len(odd)
        even_sum = sum(even)
        if k < even_sum: 
            return True 
        return (k - even_sum) % 2 == 0

start_time = time.time()
t = Solution()
root = t.canConstruct("ibzkwaxxaggkiwjbeysz", 15)

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

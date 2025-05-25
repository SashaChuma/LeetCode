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
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False 
        min_v, max_v = 0,0
        for p, flag in zip(s, locked):
            if flag == "1":
                if p == "(":
                    min_v += 1
                    max_v += 1
                else:
                    if min_v > 0:
                        min_v -= 1
                    max_v -= 1
                    if max_v < 0:
                        return False
            else:
                if min_v > 0:
                    min_v -= 1
                max_v += 1
        return min_v == 0
start_time = time.time()
t = Solution()
root = t.canBeValid("))()))", "010100")

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

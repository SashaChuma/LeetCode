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
    def lemonadeChange(self, bills: List[int]) -> bool:
        f = 0
        t = 0
        for b in bills:
            if b == 5:
                f += 1
            elif b == 10:
                f -= 1
                t += 1
                if f < 0:
                    return False
            else:
                if t > 0:
                    t -=1
                    f -= 1
                else: 
                    f -= 3
                if f < 0 or t < 0: 
                    return False
        return True
start_time = time.time()
t = Solution()
root = t.lemonadeChange([5,5,5,10,20])
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

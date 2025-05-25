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
    def smallestNumber(self, pattern: str) -> str:
        s = []
        def check(ind) -> bool:
            if ind == n:
                return True
            last = int(s[-1])
            if pattern[ind] == "D":
                for j in range(1, last):
                    if used[j] == 0:
                        used[j] = 1
                        s.append(j)
                        if (check(ind+1)):
                            return True
                        s.pop()
                        used[j] = 0
            if pattern[ind] == "I":
                for j in range(last+1, 10):
                    if used[j] == 0:
                        used[j] = 1
                        s.append(j)
                        if (check(ind+1)):
                            return True
                        s.pop()
                        used[j] = 0
            return False
        n = len(pattern)
        used = [0]*10
        for i in range(1,10):
            used[i] = 1   
            s = [i]         
            if check(0):
                return ''.join(str(c) for c in s)
            used[i] = 0
        return ''
start_time = time.time()
t = Solution()
root = t.smallestNumber("IIIDIDDD")

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

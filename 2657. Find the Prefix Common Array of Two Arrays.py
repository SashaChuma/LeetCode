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
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        sA = set()
        sB = set()
        k = 0
        for i in range(len(A)):
            sA.add(A[i])
            if (A[i] in sB):
                k += 1
            sB.add(B[i])
            if (B[i] in sA):
                k += 1
            res.append(k)
        return res 
start_time = time.time()
t = Solution()
root = t.findThePrefixCommonArray([1,3,2,4], [3,1,2,4])

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

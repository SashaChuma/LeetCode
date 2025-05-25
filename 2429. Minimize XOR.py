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
    def minimizeXor(self, num1: int, num2: int) -> int:
        b1 = bin(num1)[2:]
        b2 = bin(num2)[2:]
        b3 = []
        c1 = sum(int(x) for x in b1)
        c2 = sum(int(x) for x in b2)
        print(b1, b2)
        if c1 < c2:
            d = c2-c1
            for i in range(len(b1)-1,-1,-1):
                if b1[i] == "0" and d > 0:
                    d -= 1
                    b3.append("1")
                else:
                    b3.append(b1[i])
            if d > 0:
                b3.append("1"*d)
            b3.reverse()
        elif c1 > c2:
            d = c1-c2
            for i in range(len(b1)-1,-1,-1):
                if b1[i] == "1" and d > 0:
                    d -= 1
                    b3.append("0")
                else: 
                    b3.append(b1[i])
            b3.reverse()
        else:
            b3 = b1
        print(''.join(b3))
        return int(''.join(b3), 2)
start_time = time.time()
t = Solution()
root = t.minimizeXor(25, 72)

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

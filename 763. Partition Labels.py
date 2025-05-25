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
    def partitionLabels(self, s: str) -> List[int]:
        def canSplit(p):
            c1 = Counter(s[:p])
            c2 = Counter(s[p:])
            for k1 in c1.keys():
                if k1 in c2:
                    return False
            return True 
        splitted = True
        result = []
        while (splitted):
            splitted = False
            for i in range(1, len(s)):
                if canSplit(i):
                    splitted = True
                    result.append(i)
                    s = s[i:]
                    break
        return result + [len(s)]
start_time = time.time()
t = Solution()
root = t.partitionLabels("ababcbacadefegdehijhklij")

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

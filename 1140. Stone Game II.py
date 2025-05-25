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
    def stoneGameII(self, piles: List[int]) -> int:
        peek_dic = defaultdict(int)
        suffix = [0]*len(piles)
        s = 0
        for i in range(len(piles)-1,-1,-1):
            s += piles[i]
            suffix[i] = s
        
        def bestPeek(m, pos, n):
            if (m,pos) in peek_dic:
                return peek_dic[(m,pos)]
            if pos+m*2 >= n:
                peek_dic[(m,pos)] = suffix[pos]
                return suffix[pos]
            min_peek = suffix[pos] 
            for i in range(1, 2*m+1):
                op_peek = bestPeek(max(m,i), pos+i, n)
                min_peek = min(op_peek, min_peek)
            peek_dic[(m,pos)] = suffix[pos]-min_peek
            return suffix[pos]-min_peek
            
        return bestPeek(1, 0, len(piles))
start_time = time.time()
t = Solution()
root = t.stoneGameII([2,7,9,4,4])
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

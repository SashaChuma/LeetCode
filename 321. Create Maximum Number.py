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
    def __init__(self):
        self.nums1 = []
        self.nums2 = []
        self.n1 = 0
        self.n2 = 0
        self.cache = {}

    def recc(self, p1, p2, l) -> str:
        if (p1,p2,l) in self.cache:
            return self.cache[(p1,p2,l)]
        if l == 0:
            return ""
        if self.n1-p1 + self.n2-p2 < l: 
            return ""
        num1 = str(self.nums1[p1]) + self.recc(p1+1, p2, l-1) if p1 < self.n1 else ""
        num2 = str(self.nums2[p2]) + self.recc(p1, p2+1, l-1) if p2 < self.n2 else ""
        num3 = self.recc(p1+1, p2, l)
        num4 = self.recc(p1, p2+1, l)
        num1 = num1 if self.isbigger(num1,num2) else num2
        num1 = num1 if self.isbigger(num1,num3) else num3
        num1 = num1 if self.isbigger(num1,num4) else num4
        self.cache[(p1,p2,l)] = num1
        return num1
    
    def isbigger(self, s1, s2):
            if len(s1) > len(s2):
                return True 
            elif len(s1) < len(s2):
                return False
            
            for c1,c2 in zip(s1, s2):
                if int(c1) > int(c2):
                    return True
                if int(c1) < int(c2):
                    return False
            return False 
    
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        self.n1 = len(nums1)
        self.n2 = len(nums2)
        self.nums1 = nums1
        self.nums2 = nums2
        return [int(c) for c in self.recc(0, 0, k)]

start_time = time.time()
t = Solution()
root = t.maxNumber([2,2,0,6,8,9,6],[5,2,4,5,3,6,2],7)
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

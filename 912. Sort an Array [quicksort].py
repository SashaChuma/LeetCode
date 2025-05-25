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
    def quicksort(self, arr, l, r):
        if l >= r: 
            return
        mid = (l+r)//2
        arr[r],arr[mid] = arr[mid], arr[r]
        
        p = arr[r]
        j = l
        for i in range(l,r):
            if p >= arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
                j += 1
        arr[r], arr[j] = arr[j], arr[r]
        self.quicksort(arr, l, j-1)
        self.quicksort(arr, j+1, r)
        
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums
start_time = time.time()
t = Solution()
root = t.sortArray([8,9,4,0,2,1,3,5,7,6])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

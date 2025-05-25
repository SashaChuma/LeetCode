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
    def heapify(self, arr, n, i):
        largest = i 
        left = 2*i+1
        right = 2*i+2
        if left < n and arr[left] > arr[largest]:
            largest = left 
        if right < n and arr[right] > arr[largest]:
            largest = right
        if i != largest:
            arr[i], arr[largest] = arr[largest], arr[i]
            #push down smaller element 
            self.heapify(arr, n, largest)
    
    def heapSort(self, arr):
        n = len(arr)
        for i in range(n//2-1, -1, -1):
            self.heapify(arr, n, i)
        #print(arr)        
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)                    
        #    print(arr)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapSort(nums)
        return nums
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(num):
            return int("".join([str(mapping[int(c)]) for c in str(num)]))
        
        return [num for converted, index, num in sorted([(convert(num), index, num) for index,num in enumerate(nums)])]
start_time = time.time()
t = Solution()
root = t.sortArray([8,9,4,0,2,1,3,5,7,6])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

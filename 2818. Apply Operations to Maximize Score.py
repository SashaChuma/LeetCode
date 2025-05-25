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
    def count_subsequent_lower_or_equal(self, arr):
        n = len(arr)
        result = [0] * n
        stack = []  
        
        for i in range(n - 1, -1, -1):
            count = 0
            while stack and arr[i] >= arr[stack[-1]]:
                idx = stack.pop()
                count += 1 + result[idx]
            
            result[i] = count
            stack.append(i)
        
        return result
    def count_left_lower_or_equal(self, arr):
        n = len(arr)
        result = [0] * n
        stack = []  

        for i in range(n):
            count = 0

            while stack and arr[i] > arr[stack[-1]]:
                idx = stack.pop()
                count += 1 + result[idx]

            result[i] = count
            stack.append(i)

        return result

    def maximumScore(self, nums: List[int], k: int) -> int:
        def count_unique_prime_factors(arr):
            max_val = max(arr)
            factor_count = [0] * (max_val + 1)

            for i in range(2, max_val + 1):
                if factor_count[i] == 0:  # i is prime
                    for j in range(i, max_val + 1, i):
                        factor_count[j] += 1

            return [factor_count[num] for num in arr]
        n = len(nums)
        weights = count_unique_prime_factors(nums)
        h = [(-x,i) for i,x in enumerate(nums)]
        heapq.heapify(h)
        result= 1
        #print(weights)
        r = self.count_subsequent_lower_or_equal(weights)
        l = self.count_left_lower_or_equal(weights)
        while h and k > 0: 
            x, i = heapq.heappop(h)
            x = -x
            j, jj = r[i]+1, l[i]+1    
            result = (result * (pow(x, min(j*jj, k), 1000000007))) % 1000000007
                
            k -= jj*j
        return result 
start_time = time.time()
t = Solution()
root = t.maximumScore([3289,2832,14858,22011], 6)

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

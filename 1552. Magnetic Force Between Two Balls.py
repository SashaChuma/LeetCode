from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
import heapq

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def calc(h) -> int:
            result = 0
            j = 0
            for i in range(n):
                if position[i]-position[j]>=h:
                    result += 1
                    j = i
                    if result == m-1:
                        return True
            return False 
        if m == 2:
            return max(position)-min(position)
        n = len(position)
        position.sort()
        right = (max(position)-min(position))//(m-1)
        left = 1
        while left < right: 
            mid = (left+right)//2
            mid_val = calc(mid)
            if mid_val: 
                left = mid+1
            else: 
                right = mid-1
        if calc(left+1):
            left+=1
        elif not(calc(left)):
            left-=1
        return left
start_time = time.time()
app = Solution()
root = app.maxDistance([5,4,3,2,1,1000000000], 2)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")



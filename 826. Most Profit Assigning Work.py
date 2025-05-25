from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
import heapq
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dp = [(difficulty[i], profit[i]) for i in range(len(profit))]
        dp.sort()
        print(dp)
        m = dp[0][1]
        for i in range(1, len(dp)):
            if dp[i][1] < m:
                dp[i] = (dp[i][0], m)
            else: 
                m = dp[i][1]
        worker.sort()
        i = 0
        res = 0
        for w in worker:
            if i == 0 and w < dp[0][0]:
                continue
            while i < len(dp)-1 and w >= dp[i+1][0]:
                i += 1
            res += dp[i][1]
        return res 

start_time = time.time()
app = Solution()
root = app.maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")



from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
import heapq
from collections import Counter
import pprint

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        
        # Create a zero matrix
        matrix = [[0] * n for _ in range(m)]
        
        # Copy row_sums and col_sums to work with them
        row_work = rowSum[:]
        col_work = colSum[:]
        
        for i in range(m):
            for j in range(n):
                # Determine the value to place in the matrix
                value = min(row_work[i], col_work[j])
                matrix[i][j] = value
                
                # Decrease the corresponding row and column sums
                row_work[i] -= value
                col_work[j] -= value
        
        return matrix
         
    
start_time = time.time()
app = Solution()
root = app.restoreMatrix([5,7,10],[8,6,8])
#root = app.calculateMinimumHP([[0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


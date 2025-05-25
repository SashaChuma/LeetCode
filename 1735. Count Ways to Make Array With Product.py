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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_m(m):
    for r in m:
        print(" ".join(f"{num:4d}" for num in r))

def read_tree(nums) -> Optional[TreeNode]:
    if len(nums) == 0 or nums[0] is None:
        return None
    root = TreeNode(nums[0])
    q = deque()
    q.append(root)
    i = 1
    while q and i < len(nums):
        node = q.popleft()
        if nums[i] is not None:
            node.left = TreeNode(nums[i])
            q.append(node.left)
        if nums[i+1] is not None:
            node.right = TreeNode(nums[i+1])
            q.append(node.right)
        i += 2 
    return root 
def write_tree(root, level=0, side=""):
    if (root):
        print(f"{side}:{level} {root.val}")
        write_tree(root.left, level+1, "L")
        write_tree(root.right, level+1, "R")
class BIT: 
    def __init__(self, size) -> None:
        size += 2
        self.data = [0]*size
        self.size = size
    def update(self, i, val):
        i += 1
        while i < self.size:
            self.data[i] += val
            i += (i & -i)
    def query(self, i):
        i += 1
        result = 0
        while i > 0:
            result += self.data[i]
            i -= (i & -i)
        return result 
import math
mod = 1000000007
    
class Solution:
    @lru_cache(-1)
    def fac(self,x):
        if x == 1:
            return 1
        return self.fac(x-1)*x
    
    @lru_cache(-1)
    def c(self, n, k):
        res = 1
        f = self.fac(k)
        d = 1
        for i in range(n-k+1,n+1):
            res *= i
            if d:
                if (res%f)==0:
                    d = 0
                    res //= f
            else:
                res = res % mod
        return res

    def primes_up_to(self, n):
        sieve = [True] * (n + 1)
        sieve[0:2] = [False, False]  # 0 and 1 are not primes

        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = False

        return [i for i, is_prime in enumerate(sieve) if is_prime]
    
    def prime_divisors(self, n, primes):
        dic = defaultdict(int)
        i = 0
        while n > 1:
            while n % primes[i] == 0:
                dic[primes[i]] += 1
                n = n // primes[i]
            i += 1
        return dic
    def idealArrays(self, n: int, maxValue: int) -> int:
        if maxValue == 1:
            return 1 
        result = 1
        primes = self.primes_up_to(maxValue)
        for x in range(2, maxValue+1):
            dic = self.prime_divisors(x, primes)
            xr = 1
            for k in dic.values():
                xr = (xr*self.c(n+k-1, k))%mod
            result = (result + xr) % mod
        return result
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        maxValue = max([q2 for _,q2 in queries])
        primes = self.primes_up_to(maxValue+1)
        result = []
        for n, x in queries:
            dic = self.prime_divisors(x, primes)
            xr = 1
            for k in dic.values():
                xr = (xr*self.c(n+k-1, k))%mod
            result.append(xr % mod)
        return result
        
start_time = time.time()
t = Solution()
root = t.waysToFillArray([[2,6],[5,1],[73,660]])        
#print(root.val)
#    root.print_tree()
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

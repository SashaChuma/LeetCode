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
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0
        def countPaths(level, node)->defaultdict:
            nonlocal res
            if not(node):
                return defaultdict(int)
            if not(node.left) and not(node.right):
                return defaultdict(int, {level:1})
            left_dic = countPaths(level+1, node.left)
            right_dic = countPaths(level+1, node.right)
            for sub_level, sub_count in left_dic.items():
                right_level = distance-(sub_level-level)+level+1 
                if right_level > 0:
                    for i in range(right_level):
                        if i in right_dic:
                            res += right_dic[i]*sub_count
            
            for l,c in left_dic.items():
                right_dic[l] += c
            return right_dic

        countPaths(0, root)

        return res
         
    
start_time = time.time()
app = Solution()
root = app.countPairs(TreeNode(78, TreeNode(15, TreeNode(73, TreeNode(30)), TreeNode(98, TreeNode(63), TreeNode(32))), TreeNode(81, TreeNode(36))), 6)
#root = app.calculateMinimumHP([[0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


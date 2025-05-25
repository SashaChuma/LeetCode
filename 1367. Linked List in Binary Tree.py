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
# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        l = []
        node = head
        while node:
            l.append(node.val)
            node = node.next
        parent_dic = {root : TreeNode(-1)}
        stack = [root]
        while stack: 
            node = stack.pop()
            if not(node):
                break
            parent = node 
            i = len(l)-1
            while i >= 0 and parent and parent.val == l[i]:
                i -= 1
                parent = parent_dic[parent]
            if i == -1:
                return True
            if node.left:
                parent_dic[node.left] = node 
                stack.append(node.left)
            if node.right:
                parent_dic[node.right] = node
                stack.append(node.right)
        return False
start_time = time.time()
t = Solution()
root = t.isSubPath(ListNode(4, ListNode(2, ListNode(2))), 
                   TreeNode(1, TreeNode(4, TreeNode(2, TreeNode(1))), 
                               TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1), TreeNode(3))))))

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

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
#class Solution:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def print_tree(self, level=0, prefix="Root: "):
        print(" " * (level * 4) + prefix + str(self.val))
        if self.left:
            self.left.print_tree(level + 1, "L--- ")
        if self.right:
            self.right.print_tree(level + 1, "R--- ")

def print_matrix(matrix, rowheader=None, colheader=None):
    if not matrix:
        print("Empty matrix")
        return    
    col_widths = [max(len(str(item)) for item in col) for col in zip(*matrix)]
    if colheader:
        if (rowheader):
            print(" ", end=" ")
        print(" ".join(f"{item:>{width}}" for item, width in zip(colheader, col_widths)))
    for i, row in enumerate(matrix):
        if rowheader: 
            print(f"{rowheader[i]:>{col_widths[0]}}", end=" ")
        print(" ".join(f"{item:>{width}}" for item, width in zip(row, col_widths)))
import bisect
from collections import deque 
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        def findRecipe(r) -> bool:
            if r in avail:
                return True 
            if r in not_avail: 
                return False
            if r in visited:
                return False
            visited.add(r)
            curr_ingr = dic[r]
            for ingr in curr_ingr:
                if ingr in avail:
                    continue
                if ingr in not_avail: 
                    not_avail.add(r)
                    return False
                if ingr in dic:
                    if not(findRecipe(ingr)):
                        not_avail.add(r)
                        return False
                else: 
                    not_avail.add(r)
                    return False
            avail.add(r)
            return True
        visited = set()
        avail = set()
        dic = {}
        not_avail = set()
        for supply in supplies:
            avail.add(supply)
        for recipe, ingred in zip(recipes,ingredients):
            dic[recipe] = ingred
        result = []
        for recipe in recipes:
            if findRecipe(recipe):
                result.append(recipe)
        return result
start_time = time.time()
t = Solution()
root = t.findAllRecipes(["ju","fzjnm","x","e","zpmcz","h","q"], [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]],
                        ["f","hveml","cpivl","d"])

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

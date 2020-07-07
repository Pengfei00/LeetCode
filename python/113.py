# 113. 路径总和 II
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
import copy
import functools
import time
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f"TreeNode{{val: {self.val}, left: {self.left}, right: {self.right}}}"

    def __bool__(self):
        return self.val is not None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        self.dfs(root, sum,[])
        print(self.res)
        return self.res

    def dfs(self, root, sum,res):
        # 深度遍历二叉树
        res = copy.deepcopy(res)
        if not root:
            return False
        if not root.left and not root.right:
            if sum == root.val:
                res.append(root.val)
                self.res.append(res)
            return
        res.append(root.val)
        self.dfs(root.left, sum - root.val,res)
        self.dfs(root.right, sum - root.val,res)


if __name__ == '__main__':
    testcase = [
        {
            "tree": [5, 4, 8, 11, None, 13, 4, 7, 2,None,None, 5, 1],
            "val": 22,
            "res": [
   [5,4,11,2],
   [5,8,4,5]
]
        },
    ]
    test = []
    for case in testcase:
        l = case['tree']
        root = None
        if l:
            root = TreeNode(l.pop(0))
            tree = [root]
            while tree and l:
                node = tree.pop(0)
                left = TreeNode(l.pop(0) if l else None)
                right = TreeNode(l.pop(0) if l else None)
                if left.val:
                    tree.append(left)
                    node.left = left
                if right.val:
                    tree.append(right)
                    node.right = right
        test.append(
            (root, case['val'], case['res'])
        )
    for i in test:
        print(Solution().pathSum(i[0], i[1]) == i[2])

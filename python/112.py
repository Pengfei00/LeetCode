# 112. 路径总和
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#
# 说明: 叶子节点是指没有子节点的节点。
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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        return self.dfs(root, sum)

    def dfs(self, root, sum):
        # 深度遍历二叉树
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.dfs(root.left, sum - root.val) or self.dfs(root.right, sum - root.val)


if __name__ == '__main__':
    testcase = [
        {
            "tree": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
            "val": 22,
            "res": True
        },
        {
            "tree": [],
            "val": 0,
            "res": False
        },
        {
            "tree": [1, 2],
            "val": 1,
            "res": False
        },
        {
            "tree":[1],
            "val":1,
            "res":True
        },
        {
            "tree":[-2,None,-3],
            "val":-5,
            "res":True
        }
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
        print(Solution().hasPathSum(i[0], i[1]) == i[2])

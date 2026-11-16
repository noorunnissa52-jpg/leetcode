# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root):
        arr = []
        def nodes(node):
            if node is None:
                return
            nodes(node.left)
            arr.append(node.val)
            nodes(node.right)
        nodes(root)
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True

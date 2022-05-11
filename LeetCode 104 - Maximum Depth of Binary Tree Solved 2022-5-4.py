"""
104. Maximum Depth of Binary Tree
Easy
Runtime: 28 ms, faster than 87.12% of Python online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.8 MB, less than 7.97% of Python online submissions for Maximum Depth of Binary Tree.

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 
Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

==========================================================================
SOLUTION
Runtime: 28 ms, faster than 87.12% of Python online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.8 MB, less than 7.97% of Python online submissions for Maximum Depth of Binary Tree.
"""

# LEETCODE DEFINITION OF THE TREE NODE (input type is a tree node, not a list)
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getDepth(node, depth):
            if node.left is None:
                depthLeft = depth
            else:
                depthLeft = getDepth(node.left, depth+1)
            
            if node.right is None:
                depthRight = depth
            else:
                depthRight = getDepth(node.right, depth+1)
            
            return max(depthLeft, depthRight)
                                      
        
        if root is None:
            return 0
        else:
            depth = 0
        
            return getDepth(root, depth+1)
        
        
        """
        []
        length = 0
        depth = 0
        
        0
        [0]
        length = 1
        depth = 1
        
         0
        1 2
        length = 3
        depth = 2 = 1 + 2
        
                 0
            1          2
         3    4     5     6
        7 8  9 10 11 12
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        length = 13 = 1 + 2 + 4 + 6 (which is less than 8).  13 < 15 so same depth as 15.
        depth = 4
        
        0
         2
          6
           14
        [0, null, 2, null, null, null, 6, null, null, null, null, null, null, null, 14]
        length = 15 = 1 + 2 + 4 + 8
        depth = 4
        
        """

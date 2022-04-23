# Create a Binary Tree Class in Python
# Goal: Make and print this binary tree
#            1
#          2     3
#       4  5   6  7
#     8 9 
# Includes creating nodes and printing only.  Excludes .add() , .insert(), .delete(), etc.

class Node:
    
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value
        
    def checkChildFull(self, node):
        childIsFull = False
        if node is not None:
            if node.left is not None and node.right is not None:
                return True   
            
    def insertValue(self, node, value):
        successFlag = False
        if node is None:
            node = Node(value)
            successFlag = True
            return successFlag
        else:
            if node.left is None:
                node.left = Node(value)
                successFlag = True
                return successFlag
            if node.right is None:
                node.right = Node(value)
                successFlag = True
                return successFlag
            
            if self.checkChildFull(node.left):
                if self.checkChildFull(node.right):
                    # if both left and right children are full,
                    # go ahead and try to insert to the left side
                    # and let the recursions eventually find an opening
                    self.insertValue(node.left, value)
                else: # right child node is not full, so try to insert there
                    self.insertValue(node.right, value)
            else: # left child node is not full, so try to insert there
                self.insertValue(node.left, value)
        return successFlag
    
    def printTree(self, node, level=0):
        # Prints a rotated binary tree, so that the root is on the left and the leaves on the right.
        # "Left" nodes visually appear below while "right" nodes visually appear above
        if node is not None:
            self.printTree(node.right, level + 1)
            print(' ' * 4 * level, node.value)
            self.printTree(node.left, level + 1)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.left = n2
n1.right = n3
n1.printTree(n1)
     3
 1
     2
     
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n2.left = n4
n2.right = n5
n4.left = n8
n4.right = n9
n3.left = n6
n3.right = n7
n1.printTree(n1)
         7
     3
         6
 1
         5
     2
             9
         4
             8

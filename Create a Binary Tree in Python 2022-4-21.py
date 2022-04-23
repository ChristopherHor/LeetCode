# Create a Binary Tree Class in Python
# Goal: Make and print this binary tree
#            1
#          2     3
#       4  5   6  7
#     8 9 
# Includes creating nodes and printing only.  Excludes .add() , .insert(), .delete(), etc.


#            1
#         2     3
#       4  5


class Node:
    def __init__(self, value = None, nodeParent = None):
        self.left = None
        self.right = None
        self.value = value
        self.parent = nodeParent
    def checkChildFull(self, node):
        childIsFull = False
        if node is not None:
            if node.left is not None and node.right is not None:
                return True   
    def findEmptyChild(self, node):
        # Returns the first empty node (node is None)
        if node is None:
            return node, node.parent
        if node.left is None:
            return 'left', node
        if node.right is None:
            return 'right', node
        if node.parent is None: # if at root of tree, prevent error of accessing the parent.right which is None.right.  Default to scanning left child
            return self.findEmptyChild(node.left)
        else:
            if node == node.parent.left:
                # If we're checking a left node, check the right node before moving downwards
                print("node was parent's left child")
                return self.findEmptyChild(node.parent.right)
            else:
                return self.findEmptyChild(node.left)    
        #return self.findEmptyChild(node.left, switchLeftRight)
        #return self.findEmptyChild(node.right, switchLeftRight)
        #return self.findEmptyChild(node.parent.right, switchLeftRight)
        #if switchLeftRight:
        #    #switchLeftRight = 1 - switchLeftRight #flip between 0 (left) and 1 (right)
        #    return self.findEmptyChild(node.right, switchLeftRight)
        #    #return self.findEmptyChild(node.parent, switchLeftRight)
        #else:
        #    switchLeftRight = 1 - switchLeftRight #flip between 0 (left) and 1 (right)
        #    return self.findEmptyChild(node.left, switchLeftRight)
    def insertValue(self, node, value):
        # Does not make balanced trees but makes somewhat balanced branches.
        successFlag = False
        if node is None:
            node = Node(value)
            successFlag = True
            return successFlag
        else:
            leftOrRight, emptyNodeParent = self.findEmptyChild(node)
            if leftOrRight == 'left':
                emptyNodeParent.left = Node(value, emptyNodeParent)
            elif leftOrRight == 'right':
                emptyNodeParent.right = Node(value, emptyNodeParent)
            else:
                print("Error: unknown leftOrRight flag: ", leftOrRight, "\n at ", emptyNodeParent.value)
                return successFlag # failure
            emptyNode = Node(value, emptyNodeParent)
            successFlag = True
            return successFlag
            #if node.left is None:
            #    node.left = Node(value, node)
            #    successFlag = True
            #    return successFlag
            #if node.right is None:
            #    node.right = Node(value, node)
            #    successFlag = True
            #    return successFlag
            #
            #if self.checkChildFull(node.left):
            #    if self.checkChildFull(node.right):
            #        # if both left and right children are full,
            #        # go ahead and try to insert to the left side
            #        # and let the recursions eventually find an opening
            #        self.insertValue(node.left, value)
            #    else: # right child node is not full, so try to insert there
            #        self.insertValue(node.right, value)
            #else: # left child node is not full, so try to insert there
            #    self.insertValue(node.left, value)
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

            ## inserNode....., level = 0, parentNode = None, switchLeftRight = 0
                ##if switchLeftRight == 0:
                ##    switchLeftRight = 1 - switchLeftRight #swaps between 0 and 1; 0 is left, 1 is right
                ##    self.insertNode(node.left, value, level+1, node, switchLeftRight)
                ##else:
                ##    switchLeftRight = 1 - switchLeftRight #swaps between 0 and 1; 0 is left, 1 is right
                ##    self.insertNode(node.right, value, level+1, node, switchLeftRight) #Only add a level deeper if for the right node
                ###go into Node2, Level=1, parent is 1, switch=1
                
            
            
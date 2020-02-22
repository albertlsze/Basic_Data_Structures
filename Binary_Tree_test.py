'''---------------------------------------------------------------------------------------------------------------------
This code's purpose is to test Binary Tree Class

---------------------------------------------------------------------------------------------------------------------'''
'''----------------------------------------------StringBuilder-------------------------------------------------------'''
from TreesAndGraphs.BinaryTreeNode import BinTreeNode
from TreesAndGraphs.BinaryInOrderTrav import InOrderTrav

print('Binary Tree Example')

valid_binary_tree = True

# construct tree
BinTree = BinTreeNode(6)
BinTree.left = BinTreeNode(3)
BinTree.left.left = BinTreeNode(1)
BinTree.left.right = BinTreeNode(4)
BinTree.right = BinTreeNode(9)
BinTree.right.left = BinTreeNode(8)
BinTree.right.right = BinTreeNode(12)
BinTree.right.right.left = BinTreeNode(10)
BinTree.right.right.right = BinTreeNode(15)

# perform In-order Traversal
order = InOrderTrav(BinTree)
print(order)

for i in range(0,len(order)-1):
    if order[i] > order[i+1]:
        valid_binary_tree = False

print('Valid Binary Tree: ' + str(valid_binary_tree))



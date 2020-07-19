from TreesAndGraphs.BinaryTreeNode import BinTreeNode

def PreorderTrav(tree: BinTreeNode):
    treeOrder = []
    stack = [tree]

    while stack:
        temp = stack[-1]
        stack.pop(-1)
        treeOrder.append(temp.root)

        if temp.right:
            stack.append(temp.right)

        if temp.left:
            stack.append(temp.left)

    return treeOrder
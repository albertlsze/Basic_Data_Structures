from TreesAndGraphs.BinaryTreeNode import BinTreeNode

def InOrderTrav(tree: BinTreeNode):
    treeOrder = []
    stack = [tree]

    while stack:
        if stack[-1].left:
            stack.append(stack[-1].left)
        else:
            treeOrder.append(stack[-1].root)
            if stack[-1].right:
                stack[-1] = stack[-1].right
            else:
                stack.pop(-1)

    return treeOrder
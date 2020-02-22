from TreesAndGraphs.BinaryTreeNode import BinTreeNode

def InOrderTrav(tree: BinTreeNode):
    treeOrder = []
    stack = [tree]

    while stack:
        while stack[-1].left is not None:
            stack.append(stack[-1].left)
        treeOrder.append(stack[-1].root)

        stack = stack[:-1]
        if not stack:
            break
        treeOrder.append(stack[-1].root)

        if stack[-1].right is not None:
            stack[-1] = stack[-1].right
        else:
            stack = stack[:-1]

    return treeOrder
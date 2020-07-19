from TreesAndGraphs.BinaryTreeNode import BinTreeNode

def PreorderTrav(tree: BinTreeNode):
    treeOrder = []
    stack = [tree]

    while stack:
        if not stack[-1].left and not stack[-1].right:
            treeOrder.append(stack[-1].root)
            stack.pop(-1)
        else:
            temp = stack[-1]

            if temp.right:
                stack.append(temp.right)
                temp.right = None

            if temp.left:
                stack.append(temp.left)
                temp.left = None

    return treeOrder
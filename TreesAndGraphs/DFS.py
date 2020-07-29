from TreesAndGraphs.BinaryTreeNode import BinTreeNode

def DFS(tree: BinTreeNode):
    treeOrder = []
    stack = [tree]

    while stack:
        temp = stack[-1]
        stack.pop(-1)
        if temp.right:
            stack.append(temp.right)
        if temp[-1].left:
            stack.append(temp.left)

        treeOrder.append(temp.root)

    return treeOrder
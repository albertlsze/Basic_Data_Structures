from TreesAndGraphs.BinaryTreeNode import BinTreeNode

def BFS(tree: BinTreeNode):
    treeOrder = []
    queue = [tree]

    while queue:
        if queue[0].left:
            queue.append(queue[0].left)

        if queue[0].right:
            queue.append(queue[0].right)

        treeOrder.append(queue[0].root)

        queue.pop(0)

    return treeOrder
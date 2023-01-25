from collections import deque


class Node:
    def __init__(self, L, R, n):
        self.left: Node = L
        self.right: Node = R
        self.value: int = n


def codewars(node):
    if node is None:
        return []

    queue = [node]
    result_list = []
    while queue:
        current_node = queue.pop()
        if current_node is not None:
            result_list.append(current_node.value)
            if current_node.right is not None:
                queue.append(current_node.right)
            if current_node.left is not None:
                queue.append(current_node.left)
    return result_list


result = codewars(Node(Node(None, Node(None, None, 4), 2),
                       Node(Node(None, None, 5), Node(None, None, 6), 3), 1))
print(result)

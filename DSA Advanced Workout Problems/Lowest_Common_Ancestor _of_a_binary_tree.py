class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):

    if root is None:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    if left:
        return left

    return right


# Create tree
root = Node(3)

root.left = Node(9)
root.right = Node(20)

root.right.left = Node(15)
root.right.right = Node(7)

p = root.right.left
q = root.right.right

answer = lowest_common_ancestor(root, p, q)

print("LCA:", answer.data)
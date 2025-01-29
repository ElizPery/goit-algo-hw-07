class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root: Node, key: int):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root: Node, key: int):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def min_value_node(node: Node):
    current = node
    while current.left:
        current = current.left
    return current.val


def max_value_node(node: Node):
    current = node
    while current.right:
        current = current.right
    return current.val


def preorder_traversal(root: Node, path=None):
    if path is None:
        path = []
    if root:
        path.append(root.val)
        preorder_traversal(root.left, path)
        preorder_traversal(root.right, path)
    return sum(path)


def delete(root: Node, key: int):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root


# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

print(min_value_node(root))
print(max_value_node(root))
print(preorder_traversal(root))
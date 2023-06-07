class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    if node is None:
        return 0
    return node.height


def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)


def right_rotate(y):
    x = y.left
    t2 = x.right

    # Perform rotation
    x.right = y
    y.left = t2

    # Update heights
    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1

    # Return new root
    return x


def left_rotate(x):
    y = x.right
    t2 = y.left

    # Perform rotation
    y.left = x
    x.right = t2

    # Update heights
    x.height = max(height(x.left), height(x.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1

    # Return new root
    return y


def insert(node, key):
    # Perform standard BST insertion
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        # Duplicate keys not allowed
        return node

    # Update height of this node
    node.height = 1 + max(height(node.left), height(node.right))

    # Check balance factor
    bf = balance_factor(node)

    # Left-Left case
    if bf > 1 and key < node.left.key:
        return right_rotate(node)

    # Right-Right case
    if bf < -1 and key > node.right.key:
        return left_rotate(node)

    # Left-Right case
    if bf > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # Right-Left case
    if bf < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    # No rotation needed
    return node


def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.key, end=" ")
        inorder_traversal(node.right)


root = None
root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 25)

print("AVL Tree traversal in order: ", end="")
inorder_traversal(root)
print()

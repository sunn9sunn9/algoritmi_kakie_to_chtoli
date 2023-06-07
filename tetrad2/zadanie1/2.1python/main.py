class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_height(node):
    if node is None:
        return -1
    else:
        return 1 + max(get_height(node.left), get_height(node.right))

def get_balance_indicator(node):
    if node is None:
        return 0
    else:
        return get_height(node.left) - get_height(node.right)

# create binary search tree
root = Node(8)
for val in [3, 10, 1, 6, 14, 4, 7, 13]:
    node = Node(val)
    curr = root
    while True:
        if val < curr.val:
            if curr.left is None:
                curr.left = node
                break
            else:
                curr = curr.left
        else:
            if curr.right is None:
                curr.right = node
                break
            else:
                curr = curr.right

# calculate balance indicator for each node
node_stack = [root]
while node_stack:
    node = node_stack.pop()
    print("Node", node.val, "has balance indicator of", get_balance_indicator(node))
    if node.right:
        node_stack.append(node.right)
    if node.left:
        node_stack.append(node.left)

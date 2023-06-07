class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            self.insert_node(self.root, new_node)

    def insert_node(self, current, new_node):
        if new_node.value < current.value:
            if current.left is None:
                current.left = new_node
            else:
                self.insert_node(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self.insert_node(current.right, new_node)

    def get_balance_indicator(self, current):
        if current is None:
            return 0

        left_height = self.get_height(current.left)
        right_height = self.get_height(current.right)
        return left_height - right_height

    def get_height(self, current):
        if current is None:
            return 0

        left_height = self.get_height(current.left)
        right_height = self.get_height(current.right)
        return 1 + max(left_height, right_height)

    def print_in_order_traversal(self, current):
        if current is None:
            return

        self.print_in_order_traversal(current.left)
        print(current.value, "(balance: ", self.get_balance_indicator(current), ")", sep="")
        self.print_in_order_traversal(current.right)

    def get_root(self):
        return self.root


tree = BinaryTree()
tree.insert(576)
tree.insert(75)
tree.insert(33)
tree.insert(43)
tree.insert(67)
tree.insert(21)
tree.insert(899)
tree.print_in_order_traversal(tree.get_root())

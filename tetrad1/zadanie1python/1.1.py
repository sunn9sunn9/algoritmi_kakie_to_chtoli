import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    def traverse_in_order(self, current_node):
        if current_node is not None:
            self.traverse_in_order(current_node.left)
            print(current_node.value, end=" ")
            self.traverse_in_order(current_node.right)

    def traverse_pre_order(self, current_node):
        if current_node is not None:
            print(current_node.value, end=" ")
            self.traverse_pre_order(current_node.left)
            self.traverse_pre_order(current_node.right)

    def traverse_post_order(self, current_node):
        if current_node is not None:
            self.traverse_post_order(current_node.left)
            self.traverse_post_order(current_node.right)
            print(current_node.value, end=" ")

    def depth(self, current_node):
        if current_node is None:
            return 0
        else:
            left_depth = self.depth(current_node.left)
            right_depth = self.depth(current_node.right)
            return max(left_depth, right_depth) + 1

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current_node, value):
        if current_node is None:
            return False
        elif current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search(current_node.left, value)
        else:
            return self._search(current_node.right, value)

    def delete_node(self, value):
        self.root = self._delete_node(self.root, value)

    def _delete_node(self, current_node, value):
        if current_node is None:
            return None
        elif value < current_node.value:
            current_node.left = self._delete_node(current_node.left, value)
            return current_node
        elif value > current_node.value:
            current_node.right = self._delete_node(current_node.right, value)
            return current_node
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            else:
                min_right_subtree = self._find_min(current_node.right)
                current_node.value = min_right_subtree.value
                current_node.right = self._delete_node(current_node.right, min_right_subtree.value)
                return current_node

    def _find_min(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node


if __name__ == "__main__":
    tree = BinarySearchTree()
    num_elements = int(input("Enter the number of elements: "))
    elements = [random.randint(1, 100) for _ in range(num_elements)]
    for element in elements:
        tree.insert(element)

    print("In-order traversal:", end=" ")
    tree.traverse_in_order(tree.root)
    print()

    print("Pre-order traversal:", end=" ")
    tree.traverse_pre_order(tree.root)
    print()

    print("Post-order traversal:", end=" ")
    tree.traverse_post_order(tree.root)
    print()

    print("Depth of the tree:", tree.depth(tree.root))

    value_to_search = int(input("Enter a value to search for: "))
    if tree.search(value_to_search):
        print(f"{value_to_search} is in the tree")
    else:
        print(f"{value_to_search} is not in the tree")

    value_to_delete = int(input("Enter a value to delete: "))
    tree.delete_node(value_to_delete)
    print("In-order traversal after deleting:", end=" ")
    tree.traverse_in_order(tree.root)
    print()

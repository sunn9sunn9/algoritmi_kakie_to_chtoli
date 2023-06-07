class Record:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_numbers = [phone_number]

    def add_phone_number(self, phone_number):
        self.phone_numbers.append(phone_number)


class TreeNode:
    def __init__(self, record):
        self.record = record
        self.left = None
        self.right = None


class PhoneBook:
    def __init__(self):
        self.root = None

    def add_record(self, name, phone_number):
        record = Record(name, phone_number)
        if self.root is None:
            self.root = TreeNode(record)
        else:
            current_node = self.root
            while True:
                if name == current_node.record.name:
                    current_node.record.add_phone_number(phone_number)
                    break
                elif name < current_node.record.name:
                    if current_node.left is None:
                        current_node.left = TreeNode(record)
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = TreeNode(record)
                        break
                    else:
                        current_node = current_node.right

    def find_record(self, name):
        current_node = self.root
        while current_node is not None:
            if name == current_node.record.name:
                return current_node.record.phone_numbers
            elif name < current_node.record.name:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def delete_record(self, name):
        self.root = self._delete_record_helper(self.root, name)

    def _delete_record_helper(self, current_node, name):
        if current_node is None:
            return None
        if name < current_node.record.name:
            current_node.left = self._delete_record_helper(current_node.left, name)
        elif name > current_node.record.name:
            current_node.right = self._delete_record_helper(current_node.right, name)
        else:
            if len(current_node.record.phone_numbers) > 1:
                current_node.record.phone_numbers.pop()
            else:
                if current_node.left is None:
                    return current_node.right
                elif current_node.right is None:
                    return current_node.left
                else:
                    min_node = self._find_min(current_node.right)
                    current_node.record = min_node.record
                    current_node.right = self._delete_record_helper(current_node.right, min_node.record.name)
        return current_node

    def _find_min(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node


phone_book = PhoneBook()

while True:
    command = input("Enter a command (add, find, delete, quit): ")
    if command == "add":
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        phone_book.add_record(name, phone_number)
    elif command == "find":
        name = input("Enter name: ")
        phone_numbers = phone_book.find_record(name)
        if phone_numbers is None:
            print("Record not found.")
        else:
            print("Phone numbers:")
            for phone_number in phone_numbers:
                print(phone_number)
    elif command == "delete":
        name = input("Enter name: ")
        phone_book.delete_record(name)
    elif command == "quit":
        break
    else:
        print("Invalid command.")

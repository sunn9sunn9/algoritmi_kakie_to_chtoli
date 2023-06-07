class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.size = 100
        self.table = [None] * self.size

    def hash_function(self, key):
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            return sum(ord(c) for c in key) % self.size
        else:
            raise TypeError('Invalid key type')

    def add_element(self, key, value):
        index = self.hash_function(key)
        node = self.table[index]

        if node is None:
            self.table[index] = Node(key, value)
        else:
            while node.next is not None:
                if node.key == key:
                    node.value = value
                    return
                node = node.next

            if node.key == key:
                node.value = value
            else:
                node.next = Node(key, value)

    def get_value(self, key):
        index = self.hash_function(key)
        node = self.table[index]

        values = []
        while node is not None:
            if node.key == key:
                values.append(node.value)
            node = node.next

        return values

    def remove_key(self, key):
        index = self.hash_function(key)
        node = self.table[index]

        if node is None:
            return

        if node.key == key:
            self.table[index] = node.next
            return

        prev = node
        node = node.next
        while node is not None:
            if node.key == key:
                prev.next = node.next
                return
            prev = node
            node = node.next

    def print_table(self):
        for i in range(self.size):
            node = self.table[i]
            if node is not None:
                while node is not None:
                    print(f'{node.key}: {node.value}')
                    node = node.next


phone_book = HashTable()

phone_book.add_element('Smith', '555-1234')
phone_book.add_element('Johnson', '555-5678')
phone_book.add_element('Smith', '555-4321')
phone_book.add_element('Williams', '555-9876')

print(phone_book.get_value('Smith'))

phone_book.remove_key('Smith')

print(phone_book.get_value('Smith'))

phone_book.print_table()

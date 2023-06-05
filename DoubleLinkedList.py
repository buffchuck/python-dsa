class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        if self.length == 0:
            self.append(value)
        else:
            new_node = Node(value)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range((self.length - index) - 1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        if self.length == 0:
            return False
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if self.length == 0:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index)
        if temp:
            new_node = Node(value)
            new_node.next = temp
            temp.prev.next = new_node
            new_node.prev = temp.prev
            temp.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if self.length == 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        if temp:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def swap_first_last(self):
        if self.length == 0:
            return False
        if self.length == 1:
            return True
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp
        return True

    def reverse(self):
        if self.length == 0:
            return False
        if self.length == 1:
            return True
        current_node = self.head
        for _ in range(self.length):
            temp = current_node.next
            current_node.next = current_node.prev
            current_node.prev = temp
            current_node = current_node.prev  # This tripped me up for a while
        temp = self.tail
        self.tail = self.head
        self.head = temp
        return True

    def is_palindrome(self):
        if self.length == 0:
            return False
        if self.length == 1:
            return True
        stack = []
        current = self.head
        for _ in range(self.length):
            stack.append(current.value)
            current = current.next
        current = self.head
        for _ in range(self.length):
            if current.value != stack.pop():
                return False
            current = current.next
        return True

    def swap_pairs(self):
        if self.length <= 1:
            return self
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        self.head.previous = dummy

        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next

            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            second_node.prev = prev
            first_node.prev = second_node
            if first_node.next:
                first_node.next.prev = first_node

            self.head = first_node.next
            prev = first_node

        self.head = dummy.next
        if self.head:
            self.head.prev = None

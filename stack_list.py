# Creating empty stack using list
class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    # Creating a push method for stack using list

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def is_balanced_parentheses(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == "(":
            stack.push(p)
        elif p == ")":
            if stack.is_empty() or stack.pop() != "(":
                return False
    return stack.is_empty()


def reverse_string(my_string):
    temp_stack = Stack()
    new_string = ""

    for s in my_string:
        temp_stack.push(s)

    while not (temp_stack.is_empty()):
        new_string += temp_stack.pop()
    return new_string


my_string = "hello"

print(reverse_string(my_string))

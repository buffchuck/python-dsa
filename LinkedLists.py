class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
        
class LinkedList:
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
            
    def make_empty(self):
        self.head = None
        self.length = 0
            
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.tail = None
            self.head = None
            self.length-=1
            return temp
        else:
            temp = self.head
            while temp.next:
                previous = temp
                temp = temp.next
            self.tail = previous
            self.length-=1
            return temp
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head = new_node
        self.length+=1
        return True
    
    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.length-=1
        return temp
 
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp=temp.next
            return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            previous = self.get(index - 1)
            temp = self.get(index)
            new_node.next=temp
            previous.next=new_node
        self.length+=1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0 or index == self.length - 1:
            return self.pop()
        else:
            previous = self.get(index - 1)
            temp = previous.next
            previous.next = temp.next
            temp.next = None
        self.length-=1
        return temp
        
    def reverse(self):
        if self.length == 0:
            return False
        if self.length == 1:
            return True
        
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        fast_pointer = self.head
        slow_pointer = self.head
        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        return slow_pointer.value
                
    def has_loop(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False
        
    def find_kth_from_end(self, value):
        slow=self.head
        fast=self.head
        
        for _ in range(k):
            if fast is None:
                return None
            fast=fast.next
            
        while fast:
            slow=slow.next  
            fast=fast.next
        return slow
        
    def reverse_between(self, m, n):
        if not self.head:
            return None
        
        dummy = Node(0)
        dummy.next = self.head
        previous = dummy
        
        for _ in range(m):
            previous=previous.next
            
        current = previous.next
        
        for _ in range(n-m):
            temp=current.next
            current.next=temp.next
            temp.next=previous.next
            previous.next = temp
            
        self.head=dummy.next
        
    def partition_list(self, x):
        if not self.head:
            return None
        
        dummy1 = Node(0)
        dummy2 = Node(0)
        previous1 = dummy1
        previous2 = dummy2
        current = self.head
        
        while current:
            if current.value < x:
                previous1.next = current
                previous1 = current
            else:
                previous2.next = current
                previous2 = current
            current = current.next
            
        previous2.next = None
        
        previous1.next = dummy2.next
        
        self.head = dummy1.next
            
            
    def remove_duplicates(self):
        if not self.head:
            return None
        
        nodes = set()
        current = self.head
        previous = None
        
        while current:
            if current.value not in nodes:
                nodes.add(current.value)
                previous = current
            else:
                previous.next = current.next 
                self.length-=1     
            
            current = current.next

                                                                                                                    
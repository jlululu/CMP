# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
        
    def print_value(self):
        print(self.value)
        

class LinkedList:
    def __init__(self, size = 300):
        self.header = ListNode(None)
        self.size = size
        self.count = 0
        
    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == self.size
    
    def __str__(self):
        curr_node = self.header
        s = ''
        while curr_node.next_node:
            if s:
                s = s + '->'
            s = s + str(curr_node.next_node.value)
            curr_node = curr_node.next_node
        return s
    
    def search(self, value):
        curr_node = self.header
        while curr_node.next_node:
            if curr_node.next_node.value == value:
                return True
            curr_node = curr_node.next_node
        return False
    
    def insert(self, value):
        if self.is_full():
            print("The list is full.")
            return
        node = ListNode(value)
        curr_node = self.header
        while curr_node.next_node:
            curr_node = curr_node.next_node
        curr_node.next_node = node
        self.count = self.count + 1
            
    def delete(self, value):
        if not self.count:
            print("The linkedlist is empty.")
            return
        curr_node = self.header
        while curr_node.next_node:
            if curr_node.next_node.value == value:
                temp = curr_node.next_node.next_node
                curr_node.next_node = temp
                self.count = self.count - 1
                return
            curr_node = curr_node.next_node
        print("{} is not in the linkedlist.".format(value))
    
    def traverse(self):
        values = []
        curr_node = self.header
        while curr_node.next_node:
            values.append(curr_node.next_node.value)
            curr_node = curr_node.next_node
        return values
    

           

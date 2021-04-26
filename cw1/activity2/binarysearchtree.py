# -*- coding: utf-8 -*-
import queue

class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
    def printValue(self):
        print(self.value)
        
        
class BinarySearchTree:
    def __init__(self, size = 300):
        self.root = None
        self.size = size
        #count the number of nodes in the tree
        self.count = 0
        
    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == self.size
    
    def search(self, value):
        curr_node = self.root
        while curr_node:
            if curr_node.value == value:
                return True
            elif curr_node.value > value:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return False
    
    def insert(self, value):
        if self.is_full():
            print("The tree is already full.")
            return
        node = TreeNode(value)
        if not self.root:
            self.root = node
        else:
            parent_node = None
            curr_node = self.root
            #direc = 1 means curr_node is parent_code's right child, while direc = -1 means it is the left child.
            direc = 0
            while True:
                if not curr_node:
                    if direc == 1:
                        parent_node.right = node
                    else:
                        parent_node.left = node
                    break
                elif curr_node.value >= value:
                    parent_node = curr_node
                    curr_node = curr_node.left
                    direc = -1
                else:
                    parent_node = curr_node
                    curr_node = curr_node.right
                    direc = 1
        self.count = self.count + 1
    
    def delete(self, value):
        #in case the BST is null.
        if not self.root:
            print("The tree is empty.")
            return
        if self.root.value == value:
            ''''if deleting the root node, there're three possible circumstances: 
                1.root has no left child, so that right child becomes the new root;
                2.root has no right child, so that left child becomes the new root
                3.root has both left and right child, then let the right child become the new root, due to the property of BST, we can add the original left child 
                as the left child of the most left child of the original right child'''
            leftT = self.root.left
            rightT = self.root.right
            if not leftT:
                self.root = rightT
            elif not rightT:
                self.root = leftT
            else:
                self.root = rightT
                curr_node = self.root
                while curr_node.left:
                    curr_node = curr_node.left
                curr_node.left = leftT
            self.count = self.count - 1
        else:
            parent_node = None
            curr_node = self.root
            direc = 0
            #in case there's no such value
            while curr_node:
                if curr_node.value == value:
                    leftT = curr_node.left
                    rightT = curr_node.right
                    if not leftT:
                        if direc == -1:
                            parent_node.left = rightT
                        else:
                            parent_node.right = rightT
                    elif not rightT:
                        if direc == -1:
                            parent_node.left = leftT
                        else:
                            parent_node.right = leftT
                    else:
                        if direc == -1:
                            parent_node.left = rightT
                        else:
                            parent_node.right = rightT
                        curr_node = rightT
                        while curr_node.left:
                            curr_node = curr_node.left
                        curr_node.left = leftT
                    self.count = self.count - 1
                    return
                elif curr_node.value > value:
                    parent_node = curr_node
                    curr_node = curr_node.left
                    direc = -1
                else:
                    parent_node = curr_node
                    curr_node = curr_node.right
                    direc = 1
            print("{} is not in the tree.".format(value))
            
            
    
    def traverse(self):
        '''in-order traverse: first visit the left child of the node, then the node itself, finally the right child of it.
            to do this, we can take use of the property of stack.'''
        values = []
        if not self.root:
            print("The tree is null.")
            return
        stack1 = []
        stack2 = []
        stack1.append(self.root)
        while stack1 or stack2:
            while stack1:
                curr_node = stack1.pop()
                stack2.append(curr_node)
                if curr_node.left:
                    stack1.append(curr_node.left)
            if stack2:
                curr_node = stack2.pop()
                values.append(curr_node.value)
                if curr_node.right:
                    stack1.append(curr_node.right)
        return values
    
    
    def print_tree(self):
        #level-order traverse. take use of the property of queue.
        if self.root:
            q = queue.Queue()
            q.put(self.root)
            while not q.empty():
                num_per_level = q.qsize()
                level = ''
                count = 0
                for i in range(num_per_level):
                    curr_node = q.get()
                    if curr_node:
                        count = count + 1
                        level = level + str(curr_node.value)
                        q.put(curr_node.left)
                        q.put(curr_node.right)
                    else:
                        level = level + ' '
                        q.put(None)
                        q.put(None)
                    level = level + ' '
                if count > 0:
                    print(level.rstrip())
                else:
                    return
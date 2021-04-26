# -*- coding: utf-8 -*-
from binarysearchtree import BinarySearchTree
from linkedlist import LinkedList
import random
import time
import math
import matplotlib.pyplot as plt

TREESIZE = 300

def random_tree(n):
    bst = BinarySearchTree()
    values = [random.randint(1,1001) for i in range(n)]
    for i in range(n):
        bst.insert(values[i])
    return bst


def random_list(n):
    linlist = LinkedList()
    values = [random.randint(1, 1001) for i in range(n)]
    for i in range(n):
        linlist.insert(values[i])
    return linlist


X = [i for i in range(5,301,5)]
Y = []
for s in X:
    spend_time = 0
    for i in range(1000):
        bst = random_tree(s)
        start_time = time.time()
        bst.search(42)
        end_time = time.time()
        spend_time = spend_time + end_time - start_time
    Y.append(spend_time/1000)

plt.plot(X, Y)
plt.xlabel('Size of trees')
plt.ylabel('Search time')
plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
plt.show()
''' Complexity analysis X vs Y
    Although the line is still not very smooth, but it does follow a logarithmic complexity trend. 
    The time increases when the size increases, but the slope doesn't remain the same.When the size 
    becomes larger, the slope becomes smaller, and there's no significant change in terms of the time.
'''

#ideal linear relationship t = c*n + b using n = 5 and 10: c = (t2 - t1)/5, b = t1 - 5*c
c = (Y[1] - Y[0])/5
b = Y[0] - 5*c
Y2 = [c*i + b for i in X]

#ideal logarithmic relationship t = c1*log(n) + b1 using n = 5 and 10: c1 = (t2 - t1)/[log(10) - log(5)], b1 = t1 - c1*log(5)
c1 = (Y[1] - Y[0])/(math.log(10,2) - math.log(5,2))
b1 = Y[0] - math.log(5)*c1
Y3 = [c1*math.log(i) + b1 for i in X]

plt.plot(X, Y)
plt.plot(X, Y2)
plt.plot(X, Y3)
plt.legend(['BST','Linear','Logarithmic'])
plt.xlabel('Size of trees')
plt.ylabel('Search time')
plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
plt.show()

'''Complexity analysis X vs Y, Y2 and Y3
    The BST search complexity follows more of the trend of the ideal logarithmic complexity
    rather than the ideal linear complexity. But it doesn't follow exactly the same line as 
    the ideal logarithmic complexity. I think the main reason for it is that the BST we build
    is not totally balanced. And for an unbalanced tree whose depth may be n, the searching 
    operation through it is actually very similar to a linear search which takes O(n) time.
    So in this case, what we need to do is to guarantee that our BST always keeps balanced 
    in all the insert and delete operations.
'''


Y4 = []
for s in X:
    spend_time1 = 0
    for i in range(1000):
        linlist = random_list(s)
        start_time1 = time.time()
        linlist.search(42)
        end_time = time.time()
        spend_time1 = spend_time1 + end_time - start_time1
    Y4.append(spend_time1/1000)
    
plt.plot(X, Y)
plt.plot(X, Y2)
plt.plot(X, Y3)
plt.plot(X, Y4)
plt.legend(['BST','Linear','Logarithmic','LL'])
plt.xlabel('Size of trees')
plt.ylabel('Search time')
plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
plt.show()

'''Complexity analysis X vs Y, Y2 and Y3
    As shown in the graph, the complexity of the linkedlist search follows the trend of a linear relationship,
    and its slope is even larger than the ideal linear complexity which we created before based on the BST search.
    When the size is small, the difference between the search time of BST and linkedlist is not so obvious. But as
    the size increases, the gap between BST and linkedlist is also widening. Thus, I think for small data search,
    both data structures can handle it well, while for big data search, BST is a much better choice than linkedlist.
'''

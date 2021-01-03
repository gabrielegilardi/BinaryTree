"""
Test file for the binary tree data structure in file <BinaryTree.py>

Copyright (c) 2021 Gabriele Gilardi
"""

from BinaryTree import *

# Build the tree
#
#                   0
#         1                   2
#    3         4         5         6
#  7   8     -   9     -   -     10  11
#
tree = BinaryTree(0)                        # Level 0
n1 = tree.add_left(1, parent=tree.root)     # Level 1
n2 = tree.add_right(2, parent=tree.root)
n3 = tree.add_left(3, parent=n1)            # Level 2
n4 = tree.add_right(4, parent=n1)
n5 = tree.add_left(5, parent=n2)
n6 = tree.add_right(6, parent=n2)
n7 = tree.add_left(7, parent=n3)            # Level 3
n8 = tree.add_right(8, parent=n3)
n9 = tree.add_right(9, parent=n4)
n10 = tree.add_left(10, parent=n6)
n11 = tree.add_right(11, parent=n6)

print('\n==== Info about the tree:')
# Binary tree object
# - root value = 0
# - size = 12
# - height = 3
print(tree)

print('\n==== Nodes [value, left child value, right child value, parent value]:')
# [[0, 1, 2, None], [1, 3, 4, 0], [2, 5, 6, 0], [3, 7, 8, 1], [4, None, 9, 1],
#  [5, None, None, 2], [6, 10, 11, 2], [7, None, None, 3], [8, None, None, 3],
#  [9, None, None, 4], [10, None, None, 6], [11, None, None, 6]]
print(tree_nodes(tree.root))

print('\n==== Examples of checks:')
print('- tree is empty:', tree.is_empty())          # False
print('- node n3 is a leaf:', tree.is_leaf(n3))     # False
print('- node n5 is a leaf:', tree.is_leaf(n5))     # True

print('\n==== Examples of search starting from the root:')
print(tree.search(10, order='pre'))     # Search 10 using pre-order
print(tree.search(3, order='post'))     # Search 3 using post-order
print(tree.search(5))                   # Search 5 using a qeueu

print('\n==== Examples of search in sub-trees:')
print(tree.search_in(9, n1))        # Search 9 using in-order, start from n1
print(tree.search_stack(11, n6))    # Search 11 using a stack, start from n6

print('\n==== Change value in n4 from 4 to -4:')
print(tree.change(-4, 4, order='pre'))  # Use pre-order to search
print('\n==== Change the value back using the node:')
n4.set_value(4)
print(n4)

print('\n==== Remove value 6 and node n3 and print the tree info and nodes:')
#
#                   0
#         1                   2
#    -         4         5         -
#  -   -     -   9     -   -     -   -
#
tree.remove(6)
tree.remove(n3)
print(tree)
# Binary tree object
# - root value = 0
# - size = 6
# - height = 3
print(tree_nodes(tree.root))
# [[0, 1, 2, None], [1, None, 4, 0], [2, 5, None, 0],
#  [4, None, 9, 1], [5, None, None, 2], [9, None, None, 4]]

print('\n==== Add sub-tree with root n3 to n2 and print the tree info and nodes:')
#
#                   0
#         1                   2
#    -         4         5         3
#  -   -     -   9     -   -     7   8
#
tree.add_subtree(n3, n2, side='right')
print(tree)
# Binary tree object
# - root value = 0
# - size = 9
# - height = 3
print(tree_nodes(tree.root))
# [[0, 1, 2, None], [1, None, 4, 0], [2, 5, 3, 0], [4, None, 9, 1],
#  [5, None, None, 2], [3, 7, 8, 2], [9, None, None, 4], [7, None, None, 3],
#  [8, None, None, 3]]

# Add a new node with value 20 on the right side of n2 and push the sub-tree
# already there on the left side of the new node
print('\n==== Add a new node and print the tree info and nodes:')
#
#                   0
#         1                   2
#    -         4         5         20
#  -   -     -   9     -   -     3    -
#                              7   8
#
print(tree.add_right(20, n2, side='left'))
print(tree)
# Binary tree object
# - root value = 0
# - size = 10
# - height = 4
print(tree_nodes(tree.root))
# [[0, 1, 2, None], [1, None, 4, 0], [2, 5, 20, 0], [4, None, 9, 1],
#  [5, None, None, 2], [20, 3, None, 2], [9, None, None, 4], [3, 7, 8, 2],
#  [7, None, None, 3], [8, None, None, 3]]

print('\n==== Create a new tree using n6 and print the tree info and nodes:')
new_tree = BinaryTree(n6)
print(new_tree)
# Binary tree object
# - root value = 6
# - size = 3
# - height = 1
print(tree_nodes(new_tree.root))
# [[6, 10, 11, None], [10, None, None, 6], [11, None, None, 6]]

print('\n==== Clear the tree and print the tree info and nodes:')
tree.clear()
print(tree)
# Binary tree object
# - root value = 0
# - size = 1
# - height = 0
print(tree_nodes(tree.root))
# [[0, None, None, None]]

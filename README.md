# Binary Tree and Binary Node Data Structures

Binary tree data structure using a binary node data structure.

## Reference

[Problem Solving with Algorithms and Data Structures](https://runestone.academy/runestone/books/published/pythonds/index.html), by Miller and Ranum.

## File

`BinaryTree.py` Binary tree and binary node classes.

```python
"""
BTnode Class:
__init__()          Initializes the node and its linked nodes.
__repr__()          Returns the string representation of the node.
set_value()         Sets/replaces the content of the node.
get_value()         Returns the content of the node.
set_right()         Sets/replaces the linked right node.
get_right()         Returns the linked right node.
set_left()          Sets/replaces the linked left node.
get_left()          Returns the linked left node.
set_parent()        Sets/replaces the linked parent node.
get_parent()        Returns the linked parent node.

BinaryTree Class:
__init__()          Initializes the binary tree with a root node.
__repr__()          Returns the string representation of the binary tree.
is_empty()          Checks if the binary tree is empty or not.
add_left()          Adds/inserts the left node of a parent.
add_right()         Adds/inserts the right node of a parent.
add_subtree         Adds a sub-tree to a parent's left/right node.
clear()             Deletes all nodes but the root.
is_leaf()           Checks if a node is a leaf or not.
search()            Searches the entire binary tree for a specific value.
search_pre()        Searches the binary tree using pre-order (recursive).
search_post()       Searches the binary tree using post-order (recursive).
search_in()         Searches the binary tree using in-order (recursive).
search_stack()      Searches the binary tree using a stack (iterative).
search_queue()      Searches the binary tree using a queue (iterative).
change()            Changes a value in the binary tree to another.
remove()            Removes a value/node/sub-tree from the binary tree.

Helper Functions:
node_info()         Returns the node information in a list.
tree_info()         Returns the number of nodes and height of a tree/sub-tree.
tree_nodes()        Returns all node information of a tree/sub-tree.
"""
```

- Five search methods: pre-order, post-order, in-order, using a stack, and
  using a queue.

- Possible to search the entire tree or only a specific sub-tree.

- Possible to add/insert a single node or a sub-tree.

- Possible to specify the value or the node object (in some of the methods).

- Possible to create a new tree from a given sub-tree.

## Examples and Notes

See *test_BinaryTree.py* for examples and *BinaryTree.py* for a few notes.

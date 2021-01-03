"""
Binary Tree and Binary Node Data Structures

Copyright (c) 2021 Gabriele Gilardi


Notes
-----
- Written and tested in Python 3.8.5.
- Binary tree class implementation using a binary node class.
- Five search methods: pre-order, post-order, in-order, using a stack, and
  using a queue.
- Possible to search the entire tree or only a specific sub-tree.
- Possible to add/insert a single node or a sub-tree.
- Possible to specify the value or the node object (in some of the methods).
- Possible to create a new tree from a given sub-tree.
- Examples of usage are in <test_BinaryTree.py>.
- Reference: "Problem Solving with Algorithms and Data Structures", by Miller
  and Ranum.


BTnode Class
------------
value               Content of the node.
right               Linked right node.
left                Linked left node.
parent              Linked parent node.
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


BinaryTree Class
----------------
root                Node at the root.
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


Helper Functions
----------------
node_info()         Returns the node information in a list.
tree_info()         Returns the number of nodes and height of a tree/sub-tree.
tree_nodes()        Returns all node information of a tree/sub-tree.
"""


from Stack import Stack
from Queue import Queue


def node_info(node):
    """
    Returns in a list the information (value, left child value, right child
    value, parent value) for the specified node.
    """
    # Node value
    node_value = node.get_value()

    # Left node value
    left_value = None
    if (node.left is not None):
        left_value = node.left.get_value()

    # Right node value
    right_value = None
    if (node.right is not None):
        right_value = node.right.get_value()

    # Parent node value
    parent_value = None
    if (node.parent is not None):
        parent_value = node.parent.get_value()

    return [node_value, left_value, right_value, parent_value]


def tree_info(node):
    """
    Returns the number of nodes and the height of the sub-tree starting at
    <node>.
    """
    # Initialize the queue
    queue = Queue()

    # Add the root node and its level to the queue
    queue.enqueue((node, 0))

    # Loop until the queue is empty
    size = 0
    height = 0
    while (not queue.is_empty()):

        # Get the last node from the queue
        node, level = queue.dequeue()
        size += 1

        # If it has a left child put it in the queue with its level
        left_child = node.get_left()
        if (left_child is not None):
            queue.enqueue((left_child, level+1))
            height = max(height, level+1)

        # If it has a right child put it in the queue with its level
        right_child = node.get_right()
        if (right_child is not None):
            queue.enqueue((right_child, level+1))
            height = max(height, level+1)

    return size, height


def tree_nodes(node):
    """
    Returns in a list of lists the node information in the tree/sub-tree
    starting at <node>.
    """
    node_list = []

    # Initialize the queue
    queue = Queue()

    # Add the root node and its level to the queue
    queue.enqueue(node)

    # Loop until the queue is empty
    while (not queue.is_empty()):

        # Get the last node from the queue and append its info
        node = queue.dequeue()
        node_list.append(node_info(node))

        # If it has a left child put it in the queue
        left_child = node.get_left()
        if (left_child is not None):
            queue.enqueue(left_child)

        # If it has a right child put it in the queue
        right_child = node.get_right()
        if (right_child is not None):
            queue.enqueue(right_child)

    return node_list


class BTnode:
    """
    Binary tree node class.
    """
    def __init__(self, value, left=None, right=None, parent=None):
        """
        Initializes the node content and (if specified) the linked left, right,
        and parent nodes.
        """
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        """
        Returns the string representation of the node.
        """
        info = node_info(self)
        return ("\nBTnode object \
                 \n- value = {} \
                 \n- left child value = {} \
                 \n- right child value = {} \
                 \n- parent value = {}" \
                .format(info[0], info[1], info[2], info[3]))

    def set_value(self, value):
        """
        Sets/replaces the content of the node.
        """
        self.value = value

    def get_value(self):
        """
        Returns the content of the node.
        """
        return self.value

    def set_left(self, left):
        """
        Sets/replaces the linked left node.
        """
        self.left = left

    def get_left(self):
        """
        Returns the linked left node.
        """
        return self.left

    def set_right(self, right):
        """
        Sets/replaces the linked right node.
        """
        self.right = right

    def get_right(self):
        """
        Returns the linked right node.
        """
        return self.right

    def set_parent(self, parent):
        """
        Sets/replaces the linked parent node.
        """
        self.parent = parent

    def get_parent(self):
        """
        Returns the linked parent node.
        """
        return self.parent


class BinaryTree:
    """
    Binary tree class
    """
    def __init__(self, data):
        """
        Initializes the binary tree with an already existing node object <data >
        or creating a new one with value equal to <data>.
        """
        # If <data> is a node
        if (isinstance(data, BTnode)):
            self.root = data
            data.set_parent(None)

        # If <data> is a value
        else:
            self.root = BTnode(data)

    def __repr__(self):
        """
        Returns the string representation of the binary tree.
        """
        size, height = tree_info(self.root)
        return ("\nBinary tree object \
                 \n- root value = {} \
                 \n- size = {} \
                 \n- height = {}" \
                .format(self.root.get_value(), size, height))

    def is_empty(self):
        """
        Returns <True> if the binary tree is empty (only the root node) and
        <False> if it is not.
        """
        return self.is_leaf(self.root)

    def add_left(self, value, parent, side='left'):
        """
        Adds the specified value to the parent's left node and returns the new
        node object. If the left node is already defined, pushes that sub_tree
        down one level on the side specified by <side>.
        """
        # If no left node is defined
        if (parent.left is None):
            new_node = BTnode(value, parent=parent)

        # If the left node is defined push the old one down one level
        else:

            # Old left node
            old_node = parent.left

            # Push it on the right side of the new node
            if (side == 'right'):
                new_node = BTnode(value, right=old_node, parent=parent)

            # Push it on the left side of the new node (default)
            else:
                new_node = BTnode(value, left=old_node, parent=parent)

            # Old node new parent
            old_node.set_parent(new_node)

        # Parent new left node
        parent.set_left(new_node)

        return new_node

    def add_right(self, value, parent, side='right'):
        """
        Adds the specified value to the parent's right node and returns the new
        node object. If the right node is already defined, pushes that sub_tree
        down one level on the side specified by <side>.
        """
        # If no right node is defined
        if (parent.right is None):
            new_node = BTnode(value, parent=parent)

        # If the right node is defined push the old one down one level
        else:

            # Old left node
            old_node = parent.right

            # Push it on the left side of the new node
            if (side == 'left'):
                new_node = BTnode(value, left=old_node, parent=parent)

            # Push it on the right side of the new node (default)
            else:
                new_node = BTnode(value, right=old_node, parent=parent)

        # Parent new right node
        parent.set_right(new_node)

        return new_node

    def add_subtree(self, root, parent, side='left'):
        """
        Adds the specified sub-tree to the parent's left/right node. Anything
        already attached to that side of the parent node is overwritten.
        """
        # Set the parent for the sub-tree
        root.set_parent(parent)

        # Attach the sub-tree to the right side of the parent
        if (side == 'right'):
            parent.set_right(root)

        # Attach the sub-tree to the left side of the parent
        else:
            parent.set_left(root)

        return

    def clear(self):
        """
        Deletes all nodes but the root.
        """
        self.root.set_left(None)
        self.root.set_right(None)

    def is_leaf(self, node):
        """
        Returns <True> if the node is a leaf and <False> if it is not.
        """
        if (node.left is None and node.right is None):
            return True

        else:
            return False

    def search(self, value, order='queue'):
        """
        Searches the binary tree for a specified value and returns its node
        object. Returns <None> if the specified value is not in the binary tree.
        """
        # Search using pre-order
        if (order == 'pre'):
            node = self.search_pre(value, self.root)

        # Search using post-order
        elif (order == 'post'):
            node = self.search_post(value, self.root)

        # Search using in-order
        elif (order == 'in'):
            node = self.search_in(value, self.root)

        # Search using a stack (LIFO order)
        elif (order == 'stack'):
            node = self.search_stack(value, self.root)

        # Search using a queue (FIFO order) - default
        else:
            node = self.search_queue(value, self.root)

        return node

    def search_pre(self, value, node):
        """
        Searches the binary tree for the specified value using preorder and
        returns the corresponding node object. Returns <None> if not found.
        """
        if (node is not None):

            # Check the parent node
            if (node.get_value() == value):
                return node

            # Check the left branch
            left_branch = self.search_pre(value, node.get_left())
            if (left_branch is not None):
                return left_branch

            # Check the right branch
            right_branch = self.search_pre(value, node.get_right())
            if (right_branch is not None):
                return right_branch

        return None

    def search_post(self, value, node):
        """
        Searches the binary tree for the specified value using postorder and
        returns the corresponding node object. Returns <None> if not found.
        """
        if (node is not None):

            # Check the left branch
            left_branch = self.search_post(value, node.get_left())
            if (left_branch is not None):
                return left_branch

            # Check the right branch
            right_branch = self.search_post(value, node.get_right())
            if (right_branch is not None):
                return right_branch

            # Check the parent node
            if (node.get_value() == value):
                return node

        return None

    def search_in(self, value, node):
        """
        Searches the binary tree for the specified value using inoder and
        returns the corresponding node object. Returns <None> if not found.
        """
        if (node is not None):

            # Check the left branch
            left_branch = self.search_in(value, node.get_left())
            if (left_branch is not None):
                return left_branch

            # Check the parent node
            if (node.get_value() == value):
                return node

            # Check the right branch
            right_branch = self.search_in(value, node.get_right())
            if (right_branch is not None):
                return right_branch

        return None

    def search_stack(self, value, node):
        """
        Searches the binary tree for the specified value using a stack (LIFO
        order) and returns the corresponding node object. Returns <None> if
        not found.
        """
        # Initialize the stack
        stack = Stack()

        # Add the root node
        stack.push(node)

        # Loop until the stack is empty
        while (not stack.is_empty()):

            # Get the last node from the stack
            node = stack.pop()

            # Check the node
            if (node.get_value() == value):
                return node

            # If it has a left child put it in the stack
            left_child = node.get_left()
            if (left_child is not None):
                stack.push(left_child)

            # If it has a right child put it in the stack
            right_child = node.get_right()
            if (right_child is not None):
                stack.push(right_child)

        return None

    def search_queue(self, value, node):
        """
        Searches the binary tree for the specified value using a queue (FIFO
        order) and returns the corresponding node object. Returns <None> if
        not found.
        """
        # Initialize the queue
        queue = Queue()

        # Add the root node
        queue.enqueue(node)

        # Loop until the queue is empty
        while (not queue.is_empty()):

            # Get the last node from the queue
            node = queue.dequeue()

            # Check the node
            if (node.get_value() == value):
                return node

            # If it has a left child put it in the queue
            left_child = node.get_left()
            if (left_child is not None):
                queue.enqueue(left_child)

            # If it has a right child put it in the queue
            right_child = node.get_right()
            if (right_child is not None):
                queue.enqueue(right_child)

        return None

    def change(self, new_value, data, order='queue'):
        """
        Changes a value in the binary tree to another and returns its node
        object. Returns <None> if not found.
        """
        # If <data> is the node
        if (isinstance(data, BTnode)):
            node = data

        # If <data> is the value search its node
        else:
            node = self.search(data, order=order)

        # If the value has been found
        if (node is not None):

            # Change the node value
            node.set_value(new_value)

        return node

    def remove(self, data, order='queue'):
        """
        Removes a value/node/sub-tree from the binary tree and returns the
        node object. Returns <None> if not found.
        """
        # If <data> is the node
        if (isinstance(data, BTnode)):
            node = data

        # If <data> is the value search its node
        else:
            node = self.search(data, order=order)

        # If the value has been found
        if (node is not None):

            # Get the parent node
            parent = node.get_parent()

            # If it is on the left branch
            if (parent.get_left() == node):
                parent.set_left(None)

            # If it is on the right branch
            else:
                parent.set_right(None)

            node.set_parent(None)

        return node

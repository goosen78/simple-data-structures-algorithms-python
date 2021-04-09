#!/usr/bin/env python3
""" 
Binary Tree Script

"""


class BinaryTree:
    """
    This is class is used to create
    binary trees.
    """
    def __init__(self, value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None
    
    def set_left_branch(self, node):
        """
        Sets left branch of a a node
        @param node: left child (branch) of this node
        """
        self.leftBranch = node
    
    def set_right_branch(self, node):
        """
        Sets right branch of a a node
        @param node: right child (branch) of this node
        """
        self.rightBranch = node
        
    def set_parent(self, parent):
        """
        Sets left branch of a a node
        @param node: left child (branch) of this node
        """
        self.parent = parent
    
    def get_value(self):
        return self.value
    
    def get_left_branch(self):
        return self.leftBranch
    
    def get_right_branch(self):
        return self.rightBranch
    
    def get_parent(self):
        return self.parent
    
    def __str__(self):
        return str(self.value)


#!/usr/bin/env python3
"""
Tree Search Script

"""

from binary_tree import BinaryTree

    
def DFSBinary(root, fcn):
    stack = [root]
    # if there is an element in the stack
    # continue searching. Otherwise, return
    # False because there is no node in which
    # to search for
    while len(stack) > 0:
        print("At node " + str(stack[0].get_value()) + ".")
        # if the value at the current node 
        # is equal to the value being found
        # return True
        if fcn(stack[0]):
            return True
        # if the value of the current node
        # is not equal to the value being found        
        else:
            # pop the current node from the stack            
            temp = stack.pop(0)
            # every time you get something different
            # than None, i.e., there is a node at the
            # left branch, you insert it at the top
            # of the stack.
            if temp.get_right_branch():
                stack.insert(0, temp.get_right_branch())
            # every time you get something different
            # than None, i.e., there is a node at the
            # right branch, you insert it at the top
            # of the stack. In this way, you make
            # sure that you always have the left branch
            # at the top of the stack.
            if temp.get_left_branch():
                stack.insert(0, temp.get_left_branch())
    return False

def BFSBinary(root, fcn):
    queue = [root]
    # if there is still nodes in which to search
    # continue searching otherwise return False
    # it means that queue still has elements
    while len(queue) > 0:
        print("At node " + str(queue[0].get_value()) + ".")
        # if the value associated with the current
        # node is equal to the value which is
        # being found, return True
        if fcn(queue[0]):
            return True
        # if the value is not found yet
        else:
            # pop current node form the queue
            temp = queue.pop(0)
            # if there is a left branch 
            # put it at the end of the queue
            if temp.get_left_branch():
                queue.append(temp.get_left_branch())
            # if there is right branch,
            # put it at the end of the queue
            # In this way, we are making sure
            # that BFS is being performed
            # because after finishing a level
            # we go to the next level 
            if temp.get_right_branch():
                queue.append(temp.get_right_branch())
    return False

def DFSBinaryOrdered(root, fcn, ltFcn):
    """
    This Depth First Search algorithm works
    when the tree is ordered.
    """
    stack = [root]
    # if there are still nodes in the stack
    # in which to search continue searching.
    # Otherwise, return False.
    while len(stack) > 0:
        print("At node " + str(stack[0].get_value()) + ".")
        # if the current node's value equals
        # that value we are looking for
        # return True
        if fcn(stack[0]):
            return True
        # if the value we are looking
        # for is less than the current nodes's
        # value, pop the current node
        # and add its left branch (ignoring right branch)
        elif ltFcn(stack[0]):
            temp = stack.pop(0)
            if temp.get_left_branch():
                stack.insert(0, temp.get_left_branch())
        # Otherwise, it means the value
        # we are looking for is greater than the current
        # we need to pop the current node
        # and add its right branch (ignoring the left one)
        else:
            temp = stack.pop(0)
            if temp.get_right_branch():
                stack.insert(0, temp.get_right_branch())
    return False

def DFSBinaryPath(root, fcn):
    queue = [root]
    while len(queue) > 0:
        if fcn(queue[0]):
            return TracePath(queue[0])
        else:
            temp = queue.pop(0)
            if temp.get_right_branch():
                queue.insert(0, temp.get_right_branch())
            if temp.get_left_branch():
                queue.insert(0, temp.get_left_branch())
    return False


def TracePath(node):
    if not node.get_parent():
        return [node]
    else:
        return [node] + TracePath(node.get_parent())

# defining binary tree
# defining nodes
n5 = BinaryTree(5)
n2 = BinaryTree(2)
n1 = BinaryTree(1)
n4 = BinaryTree(4)
n8 = BinaryTree(8)
n6 = BinaryTree(6)
n7 = BinaryTree(7)
n3 = BinaryTree(3)
# defining branches
n5.set_left_branch(n2)
n2.set_parent(n5)
n5.set_right_branch(n8)
n8.set_parent(n5)
n2.set_left_branch(n1)
n1.set_parent(n2)
n2.set_right_branch(n4)
n4.set_parent(n2)
n8.set_left_branch(n6)
n6.set_parent(n8)
n6.set_right_branch(n7)
n7.set_parent(n6)
n4.set_left_branch(n3)
n3.set_parent(n4)

def find6(node):
    return node.get_value() == 6

def find10(node):
    return node.get_value() == 10

def find2(node):
    return node.get_value() == 2

def lt6(node):
    return node.get_value() > 6

def performTreeSearch(functions, numbers, messages):
    print(messages[0])
    for i in range(len(numbers)):
        print("Looking for " + str(numbers[i]))    
        print(messages[1] +  str(numbers[i]) + " was " + \
              ("not " if not DFSBinary(n5, functions[i]) else "")  + "found.\n")

print("DFS path")
pathTo6 = DFSBinaryPath(n5, find6)
nodes = [e.get_value() for e in pathTo6]
nodes.reverse()
for i in range(len(nodes)):    
    print("Node " + str(nodes[i]) + (" --> " if i != len(nodes) - 1 else ""),
          end="")
print(".")

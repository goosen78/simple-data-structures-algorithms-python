#!/usr/bin/env python3
""" 
Decision Tree Script

"""

from binary_tree import BinaryTree

def buildDecisionTree(sofar, todo):
    """
    @return: decision tree root which contains all references to other nodes
    """
    if len(todo) == 0:
        return BinaryTree(sofar)
    else:
        withElement = buildDecisionTree(sofar + [todo[0]], todo[1:])
        withoutElement = buildDecisionTree(sofar, todo[1:])
        here = BinaryTree(sofar)
        here.set_left_branch(withElement)
        here.set_right_branch(withoutElement)
        return here

def DFSDTree(root, valueFcn, constraintFcn):
    stack = [root]
    best = None
    visited = 0
    while len(stack) > 0:
        visited += 1
        if constraintFcn(stack[0].get_value()):
            if best == None:
                best = stack[0]
                print(best.get_value())
            elif valueFcn(stack[0].get_value()) > valueFcn(best.get_value()):
                best = stack[0]
                print(best.get_value())
            temp = stack.pop(0)
            # pop right branch if it exists (at the top of the stack)
            if temp.get_right_branch():
                stack.insert(0, temp.get_right_branch())
            # pop left branch if it exists (at the top of the stack)
            if temp.get_left_branch():
                stack.insert(0, temp.get_left_branch())
        else:            
            stack.pop(0)
    print("visited", visited)
    return best

def BFSDTree(root, valueFcn, constraintFcn):
    queue = [root]
    best = None
    visited = 0
    while len(queue) > 0:
        visited += 1
        if constraintFcn(queue[0].get_value()):
            if best == None:
                best = queue[0]
                print(best.get_value())
            elif valueFcn(queue[0].get_value()) > valueFcn(best.get_value()):
                best = queue[0]
                print(best.get_value())
            temp = queue.pop(0)
            # append right branch if it exists (at the end of the queue)
            if temp.get_left_branch():
                queue.append(temp.get_left_branch())
            # append left branch if it exists (at the end of the queue)
            if temp.get_right_branch():
                queue.append(temp.get_right_branch())
        else:
            queue.pop(0)
    print("visited", visited)
    return best

a = [6,3]
b = [7,2]
# c = [8,4]
# d = [9,5]

treeTest = buildDecisionTree([], [a,b])

def sumValues(lst):
    vals = [e[0] for e in lst]
    return sum(vals)

def sumWeights(lst):
    wts = [e[1] for e in lst]
    return sum(wts)

def WeightsBelow10(lst):
    return sumWeights(lst) <= 10

def WeightsBelow6(lst):
    return sumWeights(lst) <= 6

print("\nDFS decision tree")
foobar = DFSDTree(treeTest, sumValues, WeightsBelow10)
print(foobar.get_value())

print("\nBFS decision tree")
foobarnew = BFSDTree(treeTest, sumValues, WeightsBelow10)
print(foobarnew.get_value())
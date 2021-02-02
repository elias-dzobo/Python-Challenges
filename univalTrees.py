"""

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

"""

class Node:

    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item



def postorder(root):

    count = 0
    if (root != None):
        a = root.val
        b = root.left.val
        c = root.right.val

        if (a == b == c):
            count = count + 1

        count + postorder(root.left)
        count + postorder(root.right)

    return count

n1 = Node(5)
n2 = Node(5)
n3 = Node(5)
n4 = Node(2)
n5 = Node(5)
n6 = Node(2)
n7 = Node(2)
n8 = Node(3)
n9 = Node(1)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n4.left = n6
n4.right = n7
n3.left = n8
n3.right = n9

print(postorder(n1))
        
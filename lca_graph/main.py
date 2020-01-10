#!/usr/bin/env python

class Node:
    """
    This class is for just making the graph.
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def find_lca(root, node1, node2):
    """
    This function return node of the LCA of two given values node1 and node2. 
    This function assumes that node1 and node2 are present in the Binary Tree
    """
    if not root:
        return None

    # If either node1 or node2 matches with root's key, report 
    # the presence by returning root (Note that if a key is 
    # ancestor of other, then the ancestor key becomes LCA 
    if root.key == node1 or root.key == node2: 
        return root

    # Look for keys in left and right subtrees 
    left_lca = find_lca(root.left, node1, node2) 
    right_lca = find_lca(root.right, node1, node2)

    # If both of the above calls does not return None, then one key 
    # is present in once subtree and other is present in other, 
    # So this node is the LCA 
    if left_lca and right_lca: 
        return root  

    # Otherwise check if left subtree or right subtree is the LCA 
    return left_lca if left_lca is not None else right_lca


if __name__ == '__main__':
    # I am making the tree according to the question
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)

    print ("LCA of 4 and 5 = ", find_lca(root, 4, 5).key)
    print ("LCA of 7 and 8 = ", find_lca(root, 7, 8).key)
    print ("LCA of 6 and 7 = ", find_lca(root, 6, 7).key)
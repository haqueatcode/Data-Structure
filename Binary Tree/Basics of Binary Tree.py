
"""
Basics of Binary Tree:
    
    - A tree
    - Must have at most 2 children
    - Root node, left child, and right child node
    
- A tree node can be root, left, or right

- A tree node contains 3 types of information
    1. data/info
    2. pointer to the left child
    3. pointer to the right child

"""

class Node:
    def __init__(self, data, left = None, right = None):
        self.left = left
        self.right = right
        self.data = data
        
class BST:
    def __init__(self):
        self.root = None
        
        
if __name__ == "__main__":
    
    root = Node(3)
    root.left = Node(5)
    root.right = Node(10)
    root.left.left = Node(15)


    
    
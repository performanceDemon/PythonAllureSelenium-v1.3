class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def dfs(root):
    if root:
        print(root.value)
        dfs(root.left)
        dfs(root.right)

# Crear un árbol binario simple
root = Node(1)
root.left = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right = Node(4)
root.left.left = Node(4)
root.left.right = Node(5)

dfs(root)
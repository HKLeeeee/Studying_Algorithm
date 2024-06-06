class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


def preorder(node):  # 전위 순회(preorder Traversal)
    print(node, end='')
    if tree[node].left != '.':
        preorder(tree[node].left)
    if tree[node].right != '.':
        preorder(tree[node].right)


def inorder(node):  # 중위 순회(Inorder Traversal)
    if tree[node].left != '.':
        inorder(tree[node].left)
    print(node, end='')
    if tree[node].right != '.':
        inorder(tree[node].right)


def postorder(node):  # 후위 순회(Postorder Traversal)
    if tree[node].left != '.':
        postorder(tree[node].left)
    if tree[node].right != '.':
        postorder(tree[node].right)
    print(node, end='')


N = int(input())
tree = {}
for i in range(N):
    a, b, c = input().split()
    tree[a] = Node(a, b, c)

preorder('A')
print()
inorder('A')
print()
postorder('A')

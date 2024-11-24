class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


def preorder(node):  # 전위 순회(preorder Traversal) 루트 - 왼쪽 - 오른쪽
    print(node, end='')
    if tree[node].left != '.':
        preorder(tree[node].left)
    if tree[node].right != '.':
        preorder(tree[node].right)


def inorder(node):  # 중위 순회(Inorder Traversal) 왼쪽 - 루트 - 오른쪽
    if tree[node].left != '.':
        inorder(tree[node].left)
    print(node, end='')
    if tree[node].right != '.':
        inorder(tree[node].right)


def postorder(node):  # 후위 순회(Postorder Traversal) 왼쪽 - 오른쪽 - 루트
    if tree[node].left != '.':
        postorder(tree[node].left)네넼
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

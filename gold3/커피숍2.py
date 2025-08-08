import sys
from math import ceil, log
input = sys.stdin.readline

def make_tree(n, arr):
    tree = [0] * 2**(ceil(log(n, 2) + 1))
    def make(node, s, e):
        if s == e:
            tree[node] = arr[s]
            return tree[node]

        mid = (s + e) // 2
        tree[node] = make(node * 2 + 1, s, mid) + make(node * 2 + 2, mid + 1, e)
        return tree[node]
    make(0, 0, n - 1)
    return tree
    
def find_tree(tree, x, y, node, s, e): 
    #범위에서 벗어나면 0을 return
    if x > e or y < s: return 0
    #해당 node의 값이 범위 안에 있는 값이라면 해당 node의 값을 return
    if x <= s and e <= y:return tree[node]
    mid = (s + e) // 2
    return find_tree(tree, x, y, node * 2 + 1, s, mid) + find_tree(tree, x, y, node * 2 + 2, mid + 1, e)

def update_tree(tree, idx, num, node, s, e):
    if s == e: 
        tree[node] = num
        return
    mid = (s + e) // 2
    if s <= idx <= mid:
        update_tree(tree, idx, num, node * 2 + 1, s, mid)     
    else: 
        update_tree(tree, idx, num, node * 2 + 2, mid + 1, e)
    tree[node] = tree[node * 2 + 1] + tree[node * 2 + 2]
    
N, Q = map(int, input().split())
arr = list(map(int, input().split()))
tree = make_tree(N, arr)

for _ in range(Q):
    X, Y, A, B = map(int, input().split())
    print(find_tree(tree, min(X, Y) - 1, max(X, Y) - 1, 0, 0, N - 1))
    update_tree(tree, A - 1, B, 0, 0, N - 1)
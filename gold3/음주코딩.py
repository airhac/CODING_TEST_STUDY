import sys
from math import ceil, log2

input = sys.stdin.readline

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

def make_tree(arr):
    n = len(arr)
    size = 2 ** (ceil(log2(n)) + 1)
    tree = [1] * size

    def build(node, s, e):
        if s == e:
            tree[node] = sign(arr[s])
            return tree[node]
        mid = (s + e) // 2
        left = build(2 * node + 1, s, mid)
        right = build(2 * node + 2, mid + 1, e)
        tree[node] = left * right
        return tree[node]

    build(0, 0, n - 1)
    return tree

def query(tree, x, y, node, s, e):
    if y < s or x > e:
        return 1
    if x <= s and e <= y:
        return tree[node]
    mid = (s + e) // 2
    left = query(tree, x, y, 2 * node + 1, s, mid)
    right = query(tree, x, y, 2 * node + 2, mid + 1, e)
    return left * right

def update(tree, idx, val, node, s, e):
    if s == e:
        tree[node] = sign(val)
        return
    mid = (s + e) // 2
    if idx <= mid:
        update(tree, idx, val, 2 * node + 1, s, mid)
    else:
        update(tree, idx, val, 2 * node + 2, mid + 1, e)
    tree[node] = tree[2 * node + 1] * tree[2 * node + 2]

while True:
    try:
        line = input()
        if not line:
            break
        N, K = map(int, line.split())
        arr = list(map(int, input().split()))
        tree = make_tree(arr)
        result = []
        for _ in range(K):
            cmd = input().split()
            if cmd[0] == 'P':
                X, Y = int(cmd[1]) - 1, int(cmd[2]) - 1
                res = query(tree, X, Y, 0, 0, N - 1)
                result.append('+' if res > 0 else '-' if res < 0 else '0')
            else:
                idx, val = int(cmd[1]) - 1, int(cmd[2])
                update(tree, idx, val, 0, 0, N - 1)
        print("".join(result))
    except:
        break




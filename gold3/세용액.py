import sys

input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
result = int(1e10)
res_cand = []

for i in range(n - 2):
    left = i + 1
    right = n - 1
    
    while left < right:
        sum = arr[i] + arr[left] + arr[right]
        if abs(sum) < result:
            res_cand = [arr[i], arr[left], arr[right]]
            result = abs(sum)
            
        if sum < 0:
            left += 1
        elif sum > 0:
            right -= 1
        else:
            break
print(*res_cand)
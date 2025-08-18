import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().strip().split()))

dp = [0]

def func(num):
    length = len(dp)
    start, end = 0, length - 1
    while True:
        if (end - start) < 2:
            if dp[end] < num:
                return end
            return start
        mid = (start + end) // 2
        
        if dp[mid] == num:
            return mid - 1
        else:
            if dp[mid] > num:
                end = mid
            else:
                start = mid
for i in range(N):
    num = arr[i]
    idx = func(num) + 1
    if idx > len(dp) - 1:
        dp.append(num)
    else:
        if dp[idx] > num:
            dp[idx] = num
            
print(len(dp) - 1)
import sys

input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []

for _ in range(N):
    a, b, c, d = map(int, input().strip().split())
    
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = []
CD = []

for i in range(N):
    for j in range(N):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])
        
AB.sort()
CD.sort()        

answer = 0
left, right = 0, len(AB) - 1

while 0 <= right and left < len(AB):
    sum = AB[left] + CD[right]
    
    if sum < 0:
        left += 1 
    elif sum > 0:
        right -= 1
    else:
        x = 0
        for i in range(left + 1, len(AB)):
            if AB[left] == AB[i]:
                x += 1
            else:
                break
            
        y = 0
        for i in range(right - 1, -1, -1):
            if CD[right] == CD[i]:
                y += 1
            else:
                break
        
        left += x
        right += y
        answer += x * y
        
print(answer)


################
# import sys

# N = int(sys.stdin.readline())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# arr = tuple(map(sorted, zip(*arr)))

# AB = [a+b for a in arr[0] for b in arr[1]]
# CD = [c+d for c in arr[2] for d in arr[3]]
# AB.sort()
# CD.sort()
# count = 0

# i, j = 0, len(CD)-1
# while i<len(AB) and j >= 0:
#     if (sumval := AB[i]+CD[j]) == 0:
#         ni, nj = i+1, j-1
#         while ni < len(AB) and AB[i] == AB[ni]:
#             ni += 1
#         while nj >= 0 and CD[j] == CD[nj]:
#             nj -= 1
#         count += (ni-i)*(j-nj)
#         i, j = ni, nj
#     elif sumval < 0:
#         i += 1
#     else:
#         j -= 1
# print(count)
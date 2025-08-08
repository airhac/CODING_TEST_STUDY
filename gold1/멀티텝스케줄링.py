import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
outlet = []
answer = 0

for i in range(K):
    if arr[i] in outlet:
        continue
    
    if len(outlet) < N:
        outlet.append(arr[i])
        continue
    #우선순위의 인덱스를 저장
    priority = []
    for r in outlet:
        if r in arr[i:]:
            priority.append(arr[i:].index(r))
        else:
            priority.append(101)
            
    target = priority.index(max(priority))
    outlet.remove(outlet[target])
    outlet.append(arr[i])
    answer += 1
    
print(answer)


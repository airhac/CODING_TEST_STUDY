import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = 0
train = [0] * N

for _ in range(M):
    command = input().strip().split()
    
    com = int(command[0])
    num = int(command[1])
    if com == 1:
        sit = int(command[2]) - 1
        if not (1 << sit) & train[num - 1]:
            train[num - 1] |= (1 << sit)
    elif com == 2:
        sit = int(command[2]) - 1
        if (1 << sit) & train[num - 1]:
            train[num - 1] &= ~(1 << sit)
    elif com == 3:
        train[num - 1] <<= 1
        if (1 << 20) & train[num - 1]:
            train[num - 1] &= ~(1 << 20)
    else:
        train[num - 1] >>= 1
        
answer = len(set(train))
print(answer)


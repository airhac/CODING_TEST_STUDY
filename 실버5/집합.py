import sys

input = sys.stdin.readline
M = int(input())
S = 0
for _ in range(M):
    command = input().strip().split()
    
    if command[0] == 'add':
        num = int(command[1]) - 1 
        if (1 << num) & S:
            continue
        else:
            S |= (1 << num)
    elif command[0] == 'remove':
        num = int(command[1]) - 1 
        if (1 << num) & S:
            S &= ~(1 << num)
        else:
            continue
    elif command[0] == 'check':
        num = int(command[1]) - 1 
        if (1 << num) & S:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        num = int(command[1]) - 1 
        S ^= (1 << num)
    elif command[0] == 'all':
        S = (1 << 20) - 1
    else:
        S = 0
MOD = 1000000007  

def f(d, frm, to):  
    if d <= 1:  
        return campus[d][frm][to]  

    campus.setdefault(d, [[0 for _ in range(N)] for _ in range(N)])  
    if campus[d][frm][to]:  
        return campus[d][frm][to]  

    half = d // 2  
    other = half + 1 if d % 2 else half # 홀수면 +1    # half <= other  
    for k in range(N):  
        campus[d][frm][to] += f(half, frm, k) * f(other, k, to)  
        campus[d][frm][to] %= MOD  
    return campus[d][frm][to]  

N = 8  
campus = {}  
D = int(input())  

campus[1] = [  
    [0, 1, 0, 0, 0, 0, 0, 1],  
    [1, 0, 1, 0, 0, 0, 0, 1],  
    [0, 1, 0, 1, 0, 0, 1, 1],  
    [0, 0, 1, 0, 1, 0, 1, 0],  
    [0, 0, 0, 1, 0, 1, 0, 0],  
    [0, 0, 0, 0, 1, 0, 1, 0],  
    [0, 0, 1, 1, 0, 1, 0, 1],  
    [1, 1, 1, 0, 0, 0, 1, 0],  
]  





print(f(D, 0, 0))

m,n = map(int,input().split())
for i in range(m):
    temp = []
    for j in range(n):
        mat = list(map(int, input().split()))
        temp.append(mat)
    print(*temp)

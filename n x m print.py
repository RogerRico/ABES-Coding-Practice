m,n = map(int,input().split())
mat = []
for i in range(m):
    a = list(map(int,input().split()))
    mat.append(a)
for j in mat:
    print(*j)

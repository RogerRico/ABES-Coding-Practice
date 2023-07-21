m,n = map(int,input().split())
mat = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input()))
    mat.append(row)
for row in mat:
    print(min(row))

N = int(input())
summ = 0
for i in range(N):
    M = int(input())
    number = list(map(int,input().split()))
    for j in range(M):
        summ = summ + number[j]
    print(summ)
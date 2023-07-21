a = int(input())
ary1 = list(map(int,input().split()))
ary2 = list(map(int,input().split()))
ary3 = ary1 + ary2
ary3.sort()
m = ary3[a-1]
n = ary3[a]
d = m + n
print(d)
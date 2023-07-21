T = input()
vowel = 0
conso = 0
for j in T:
    if( j=="a" or j=="e" or j=="i" or j=="o" or j=="u" ):
        vowel += 1
    else:
        conso += 1
if( conso >= 4):
    print("YES it is easy to pronounce")
else:
    print("NO it is not easy to pronounce")
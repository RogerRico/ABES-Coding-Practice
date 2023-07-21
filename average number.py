n = int(input("Please enter the number n "))
sum = 0
for i in range(0, n+1):
    print(i)
    sum = sum + i
average = sum/n
print("Sum of n numbers is ", sum)
print("Average of n numbers is ", average)
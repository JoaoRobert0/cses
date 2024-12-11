# Author: João Roberto
# Date: 12/11/2024
# Input:
# 5
# 2 3 1 5
# Output:
# 4
 
n = int(input())
numbers = sorted(list(map(int, input().split())))
 
if numbers[n - 2] != n: # O(1)
    print(n)
 
for i in range(n - 1): # O(n)
    if numbers[i] != i + 1:
        print(i + 1)
        break
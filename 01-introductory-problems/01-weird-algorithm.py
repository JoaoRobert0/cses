# Author: João Roberto
# Date: 12/11/2024
# Input: 3
# Output: 3 10 5 16 8 4 2 1

n = int(input())

while (n != 1):
    print(n, end=' ')
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1

print(n)
import sys
from math import gcd
input = sys.stdin.readline

N = int(input())

num = [int(input()) for _ in range(N)]
num.sort()
numbers = [abs(num[i] - num[i-1]) for i in range(1, len(num))]
two_gcd = numbers[0]
for n in numbers[1:]:
    two_gcd = gcd(two_gcd, n)
candi = set()
for i in range(2, int(two_gcd ** (0.5) + 1)):
    if two_gcd%i == 0:
        candi.add(int(two_gcd//i))
        candi.add(i)
candi.add(two_gcd)
candi = list(candi)
candi.sort()
print(*candi)


# 6 45 84 > 빼준 값들의 최대공약수의 약수
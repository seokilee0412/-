import sys
from math import gcd
input = sys.stdin.readline

N, S= map(int, input().split())

pos = list(map(int, input().split()))
pos.append(S)
numbers = []
for i in range(1, len(pos)):
    numbers.append(abs(pos[i] - pos[i-1]))

g = numbers[0]
for n in range(1, len(numbers)):
    g = gcd(numbers[n], g)

print(g)
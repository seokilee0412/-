import sys
input = sys.stdin.readline

T = int(input())
N = [int(input()) for _ in range(T)]
max_n = max(N)

prime = [False, False] + [True] * (max_n - 1)

for i in range(2, int(max_n**0.5)+1):
    if prime[i]:
        for j in range(2*i, len(prime), i):
            prime[j] = False
for n in N:
    count = 0
    for i in range(n//2 + 1):
        if prime[i] and prime[n-i]:
            count += 1
    print(count)
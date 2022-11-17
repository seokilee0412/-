import sys
input = sys.stdin.readline

num = [int(n) for n in input().split('\n')[0]]

num.sort(reverse=True)

print(*num, sep='')
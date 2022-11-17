import sys
# from math import gcd
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
sub_A = list(map(int, input().split()))
A = 1
for i in sub_A:
    A *= i

M = int(input())
sub_B = list(map(int, input().split()))
B = 1
for i in sub_B:
    B *= i

def gcd(a,b):
    if a%b != 0:
        return gcd(b, a%b)
    else:
        return b


result = gcd(A,B) #or using math gcd

result = str(result)
if len(result) > 9:
    print(result[len(result) - 9:])
else:
    print(result)
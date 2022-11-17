# 개미 전사
from re import L


n = int(input())

array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2,n):
    d[i] = max(d[i -1], d[i -2] + array[i])
print(d[n-1])

# 1로 만들기
x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i -1] + 1

    if i % 2 == 0:
        d[i] == min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] == min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] == min(d[i], d[i//5] + 1)

print(d[x])

# 효율적인 화폐 구성
n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))
d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1 )

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

# 금광
for tc in range(int(input())):
    n,m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    
    for j in range(1,m):
        for i in range(n):
            if i == 0: left_up =0
            else: left_up = dp[i-1][j-1]

            if i==n-1: left_down = 0
            else: left_down = dp[i+1][j-1]

            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)

# 병사 배치하기
'''
이 문제의 기본 아이디어는 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence, LIS)로 알려진 전형적인 다이나믹 프로그래밍 문제의 아이디어와 같다
예를 들어 하나의 수열 array = {4,2,5,8,4,11,15}
    이 수열의 가장 긴 증가하는 부분 수열은 {4,5,8,11,15}

본 문제는 가장 긴 감소하는 부분 수열을 찾는 문제로 치환
LIS 알고리즘을 조금 수정하여 적용함으로써 정답을 도출 가능

'''
n = int(input())
array = list(map(int, input().split()))
array.reverse() # 본 문제는 가장 긴 감소하는 부분 수열이므로 뒤집어서 LIS 적용

dp = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
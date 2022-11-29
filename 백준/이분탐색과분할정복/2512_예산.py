import sys

input = sys.stdin.readline

N = int(input())

prices = list(map(int, input().split()))
total_price = int(input())

low,high = 0, max(prices)

while low <= high:
    mid = (low + high) // 2
    check_prices = 0
    for p in prices:
        if p >= mid:
            check_prices += mid
        else:
            check_prices += p
    if check_prices <= total_price: 
        low = mid + 1
    else: 
        high = mid - 1
print(high)
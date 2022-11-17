# 1이 될 때까지

def count_until_one():
    num = int(input())
    k = int(input())
    cnt = 0
    while num != 1:
        if num % k == 0:
            num = num//k
            cnt += 1
        else:
            num -= 1
            cnt +=1
    return cnt

print(count_until_one())

def solution():
    n, k = map(int, input().split())

    result = 0
    while True:
        target = (n//k) * k
        result += (n - target)
        n = target

        if n < k:
            break
        result += 1 # 밑 n//=k 계산 횟수 더한 것
        n //= k

# 곱하기 혹은 더하기

def sum_or_multiple():
    data = input()
    result = int(data[0])

    for i in range(1, len(data)):
        num = int(data[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num

# 모험가 길드

def split_group():
    num = int(input())
    fear = list(map(int, input().split()))
    fear.sort()

    result = 0
    count = 0

    for i in fear:
        count += 1
        if count >= i:
            result += 1
            count = 0

    print(result)


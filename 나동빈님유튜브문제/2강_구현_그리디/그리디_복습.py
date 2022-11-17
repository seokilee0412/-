# 거스름 돈

def exchange_money():
    N = int(input())
    count = 0
    count += (N // 500)
    N = (N % 500)
    
    count += (N//100)
    N = (N % 100)

    count += (N//50)
    N = (N%50)

    count += (N//10)
    
    return count

# 1이 될 때까지

def until_one():
    N, K = map(int, input().split())
    result = 0
    while True:

        target = (N//K) * K # (23//5) * 5 -> 20
        result += (N - target) # (23 - 20) -> 3
        N = target
        if N < K:
            break
        N //= K
        result += 1

    result += (N - 1)
    return result


# 곱하기 혹은 더하기

def add_or_multiple():
    string_  = input()
    value = int(string_[0])
    for s in range(1, len(string_)):
        if string_[s] > 1 and value > 1:
            value *= string_[s]
        else:
            value += string_[s]
    print(value)


# 모험가 길드

def grouping_traveler():
    N = int(input())
    fear = list(map(int, input().split()))
    fear.sort()
    count = 0
    result = 0
    for f in fear:
        count += 1
        if f <= count:
            result += 1
            count = 0
    print(result)
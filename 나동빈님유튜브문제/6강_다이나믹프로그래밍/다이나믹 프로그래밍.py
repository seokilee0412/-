# 피보나치 수열 => 재귀함수로 구현
def fibo(x):
    if x==1 or x ==2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

#피보나치 수열 ==> 다이나믹 프로그래밍으로 구현
# 메모제이션, 하향식
d = [0] * 100
n = 99
def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
print(d[n])

# 보텀업(상향식)
d = [0] * 100
d[1] = 1 
d[2] = 1
n = 99
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])
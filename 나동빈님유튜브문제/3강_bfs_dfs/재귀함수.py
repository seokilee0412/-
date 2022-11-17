def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')


recursive_function(1)

#유킬리드 호제법
def gcd(a, b):
    if a%b ==0:
        return b
    else:
        return gcd(b, a%b) 
print(gcd(192, 162)) #순서 상관없이 넣어도 동작함



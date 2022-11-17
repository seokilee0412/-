
# 최대 공약수
def gcd(a, b):
    if a%b == 0:
        return b

    else:
        return gcd(b, a%b)

def lcd(a,b):
    num = gcd(a,b)
    f = int(a//num)
    s = int(b//num)
    return num * f * s

a,b = map(int, input().split())
print(gcd(a,b))
print(lcd(a,b))
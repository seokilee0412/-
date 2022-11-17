import sys
input = sys.stdin.readline

N = int(input())

d = [0] * (N+1)
d[1] = 1
for i in range(1, N+1):
    if i < 7:
        d[i] = i
    else:
        d[i] = max(d[i-3] * 2, d[i-4] * 3, d[i-5] * 4)

print(d[N])

# d[i-4] * 3, d[i-3] * 2, d[i-5] * 4

# 8 일때
# A A A A crtl+a crtl+c crtl+V crtl+V : 12
# A A A crtl+a crtl+c crtl+v crtl+a crtl+V
# A A crtl +A crtl+c

# 10일 때
# A A A crtl +a crtl+c crtl+V crtl+a crtl+c crtl+v crtl+v: 18
# A A A A A A 

# 15 일 때
# A A A crtl +a crtl+c crtl+V crtl+V crtl+a crtl+c crtl+v crtl+v crtl+a crtl+v crtl+v : 81

# 12일 때
# A A A A crtl+a crtl+c crtl+V crtl+V crtl+a crtl+c crtl+V crtl+V: 36
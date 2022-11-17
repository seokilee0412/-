n = int(input())
d = [1] * n
d[0] = 1
for i in range(1,n):
    d[i] = d[i-1] * i
count = n -1
idx = 1
value = 0
while True:
    if count < idx:
        break

    value += d[count]// (d[idx] * d[count - idx])
    count -= 1
    idx += 1
value  = int(value) + 1
print(value % 10007)
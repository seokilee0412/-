ns = []
while True:
    n = int(input())
    if n == 0:
        break
    ns.append(n)
    
max_n = max(ns)
array = list(range(max_n * 2 + 1))
array[0] = 0
array[1] = 0
count = 0
result = []
for i in range(len(array)):
    if array[i] != 0:
        is_right = True
        if array[i] == 2:
            for k in range(0, len(array), i):
                    if k != array[i]:
                        array[k] = 0
            array[i] = 1
        else:
            for j in range(2, int(array[i]**(0.5)) + 1):
                if array[i] % j == 0:
                    is_right = False
                    break
            if is_right:
                for k in range(0, len(array), i):
                    if k != array[i]:
                        array[k] = 0
                array[i] = 1
            else:
                array[i] = 0
counts = []
for n in ns:
    count = sum(array[n+1:2*n+1])
    counts.append(count)

for c in counts:
    print(c)

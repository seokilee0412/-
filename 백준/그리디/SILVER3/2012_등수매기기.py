import sys
N = int(sys.stdin.readline())

# expected = [int(input()) for _ in range(N)]
expected = []
for _ in range(N):
    expected.append(int(sys.stdin.readline()))

expected.sort()
result = 0
idx = 1
for e in expected:
    result += abs(e - idx)
    idx += 1
print(result)
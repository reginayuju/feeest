# 1 2 3 4
# 2-1=3-2
# 1 2 4 8
# 2/1=4/2

n = int(input())

for i in range(n):
    p = list(map(int, input().split()))

    if (p[1] - p[0]) == (p[2] - p[1]):
        ans = p[3] + (p[2] - p[1])
    else:
        ans = p[3] * (p[2] // p[1])

    print(p[0], p[1], p[2], p[3], ans)

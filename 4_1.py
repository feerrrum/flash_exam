def d(x):
    ans = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            ans.add(i)
            ans.add(x // i)
    return sorted(ans)


for x in range(234432, 234568):
    if len(d(x)) == 4:
        print(x, *d(x))

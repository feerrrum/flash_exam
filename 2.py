def prime(x):
    return all(x % i != 0 for i in range(2, int(x**0.5) + 1))


def f(s):
    a = set(s)
    return len(a) == 6


ans = 2112
for x in range(100000, 1000000):
    if (x % 10 + x // 10**5) % 2 == 0 and (x // 10 % 10 % 3 == x // 10**4 % 10 % 3) \
            and (x // 10**2 % 10 + x // 10**3 % 10) < (x // 10**5 + x % 10) \
            and prime(x) and f(str(x)):
        ans -= 1
print(ans)

for a in range(100):
    f = 1
    for x in range(100):
        for y in range(100):
            if not((2 * x + 3 * y > 30) or (x + y <= a)):
                f = 0
                break
    if f:
        print(a)
        break

for n1 in '0123456789':
    for n2 in '0123456789':
        x = int('8903186' + n1 + '6' + n2 + '1')
        if x % 27 == 0:
            print(x)

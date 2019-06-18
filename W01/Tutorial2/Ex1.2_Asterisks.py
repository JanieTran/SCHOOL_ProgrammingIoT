for i in range(1, 10):
    if i <= 5:
        for j in range(i):
            print('*', end=' ')
    else:
        for j in range(10 - i):
            print('*', end=' ')
    print()
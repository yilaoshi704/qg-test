a = "{0}*{1}={2}"
for i in range(1, 10):
    for j in range(1, i + 1):
        print(a.format(i, j, j * i), end='\t')
    print('\n')

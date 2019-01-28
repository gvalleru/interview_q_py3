x = [1, 2, 3]
x = [str(i) for i in x]
x = int(''.join(x)) + 1
x = [int(i) for i in str(x)]
print(x)

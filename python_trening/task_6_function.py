def add(x, y):
    return x + y

add(1, 2)

print(add(1, 2))

def arg(a, b, c=2, d=3):
    return(type(a))

print(arg(1, 1, 1, 1))
print(arg(2, 2))
print(arg(2, 2, 1, 1))

def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(range_arg('1', '2', '3', '4'))

print(range_arg('1', '2', d= '3', c= '4'))


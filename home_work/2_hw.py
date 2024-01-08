def task_1(x: int, y: float, z: str, a: list, b: bool) -> str:
    print(type(x))
    print(type(y))
    print(type(z))
    print(type(a))
    print(type(b))

task_1(5, 3.4, 'string', [7, 9, 6], (8 > 4))

def task_2(a: int =(1, 2, 3, 5, 8, 13, 21)):
    print("a[0:3] = ", a[0:3])

task_2()

def task_3(x: int):
    print(x ** 2)

task_3(9)





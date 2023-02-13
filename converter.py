def createArray():
    create = []
    n = int(input('Введите количество эллементов создаваемого массива: '))
    for i in range(0, n):
        create.append(input("введите эллемент {} : ".format(i + 1)))
    return create
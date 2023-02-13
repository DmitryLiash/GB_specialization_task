def createArray():
    create = []
    n = int(input('Введите количество эллементов создаваемого массива: '))
    for i in range(0, n):
        create.append(input("введите эллемент {} : ".format(i + 1)))
    return create
def SerchCharacterLength(argument):
    newOne = []
    for element in argument:
        if len(element) <= 3:
            newOne.append(element)
    return newOne
print(SerchCharacterLength(createArray()))
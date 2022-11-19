import sys

print('''
Приветствуем Вас на игре "Крстики-нолики".
Для выбора ячейки, пожалуйста введите ее координаты в виде двузначного числа, 
первая цифра которого обозначает столбец, а вторая - строку.
К примеру центральная ячейка будет иметь координаты 11, а левая нижняя - 02.
Первыми ходят Крестики.
''')
# Создаем пустую сетку
grid = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]]


# Функция для печати сетки grid со вспомогательными координатами (0,1,2)
def print_grid(L):
    print(*["", 0, 1, 2], sep='\t')
    for i in range(3):
        print(i, *L[i], sep='\t')
    return ""


# Ход игрока с проверкой правильности ввода
def user_input():
    a = input(f'Ваш ход, "Игрок {turn}". Введите координаты: ')
    # Проверка введено ли пустое значение:
    while True:
        if not a.isnumeric():
            a = input(
                f'"Игрок {turn}", координаты должны быть в виде двузначного числа, каждая цифра которого равна 0,1 или 2. Попробуйте снова: ')
            continue
        hor = int(a) // 10
        ver = int(a) % 10
        # Проверка введены ли 0,1 или 2:
        if hor not in range(3) or ver not in range(3):
            a = input(
                f'"Игрок {turn}", координаты должны быть в виде двузначного числа, каждая цифра которого равна 0,1 или 2. Попробуйте снова: ')
            # Проверка свободна ли ячейка:
        elif grid[ver][hor] == "-":
            break
        else:
            a = input(f'"Игрок {turn}", данная ячейка непустая, выберите координаты пустой: ')

    return [ver, hor]


# Игровой Loop
turn = 'X'              # начинают крестики
print_grid(grid)        # Вывод пустого игрового поля
while True:
    res = user_input()
    ver, hor = res[0], res[1]   # разделение введенного значения на индексы (адрес ячейки)
    grid[ver][hor] = turn       # присвоение значения ячейке
    print_grid(grid)

    # Проверка выйграл ли кто-либо или произошла ничья:
    triple = []                 # сюда будут собираться все троицы элементов (всего их 8: 3 гориз., 3 вертик. и 2 диаг.)
    t = ''                      # для формирования отдельной троицы элементов
    for i in range(3):
        for j in range(3):
            t += grid[i][j]
        triple.append(t)
        t = ''
    for i in range(3):
        for j in range(3):
            t += grid[j][i]
        triple.append(t)
        t = ''
    triple.append(grid[0][0] + grid[1][1] + grid[2][2])
    triple.append(grid[0][2] + grid[1][1] + grid[2][0])

    if turn * 3 in triple:      # если в triple есть комбинация "ХХХ" или "ООО" значит соответствующий игрок выиграл
        print()
        print(f'Игрок {turn} выиграл! Поздравляем!')
        print()
    elif "-" not in "".join(triple):        # если пустых ячеек нет - ничья
        print("Ничья!")

    if turn * 3 in triple or "-" not in "".join(triple):
        restart = input("Xотите сыграть снова? Y = Да, N = Нет:  ").upper()
        while True:
            if restart == "Y":
                grid = [
                    ["-", "-", "-"],
                    ["-", "-", "-"],
                    ["-", "-", "-"]]
                print()
                print()
                print("НОВАЯ ИГРА")
                print_grid(grid)
                break
            elif restart == "N":
                print()
                print("Спасибо за игру! До свидания!")
                print()
                sys.exit()
            else:
                restart = input("Необходимо вписать либо Y, либо N")

    triple = []

    turn = 'X' if turn == 'Y' else 'Y'          # смена очереди

print('''
Приветствуем Вас на игре "Крстики-нолики".
Для выбора ячейки, пожалуйста введите ее координаты в виде двузначного числа, первая цифра которого обозначает столбец, а вторая - строку.
К примеру центральная ячейка будет иметь координаты 11, а правая нижняя - 22.
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


# Ход игрока
def user_input():
    a = input(f'Ваш ход "Игрок {turn}". Введите координаты: ')
    # Проверка введено ли пустое значение:
    while True:
        if a == "":
            a = input(f'"Игрок {turn}", координаты не должны быть пустыми. Попробуйте снова: ')
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
turn = 'X'                                  # начинают крестики
while True:
    res = user_input()
    ver, hor = res[0], res[1]
    grid[ver][hor] = turn
    print_grid(grid)

    # Проверка выйграл ли кто-либо или произошла ничья:
    triple = []
    t = ''
    for i in range(3):
        for j in range(3):
            t += grid[i][j]
        triple.append(t)
        t = ''
    for i in range(3):
        for j in range(3):
            t += grid[i][j]
        triple.append(t)
        t = ''
    triple.append(grid[0][0] + grid[1][1] + grid[2][2])
    triple.append(grid[0][2] + grid[1][1] + grid[2][0])

    if turn * 3 in triple:
        print(f'Игрок {turn} выйграл! Поздравляем!')
        break
    triple = []



    turn = 'X' if turn == 'Y' else 'Y'      # смена очереди



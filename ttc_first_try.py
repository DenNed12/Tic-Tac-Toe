# 1. Создаём поле:
field = [ [" ", " ", " "] for i in range(3)]
# 2.  Вывод поля на экран:
def show():
    print()
    print("   | 0 | 1 | 2 | ")
    print(" ----------------")
    for i, row in enumerate(field):
        row_string = f" {i} | {' | '.join(row)} | "
        print(row_string)
        print("----------------")

# 3. Ввод координат и проверки:
def ask():
    while True:
        cordinats = (input('    Ваш ход,введите координаты:').split())
        if len(cordinats) != 2:
            print(" Введите 2 координаты!")
            continue
        x, y = cordinats

        if not(x.isdigit()) or not(y.isdigit):
            print("Введите числа!")
            continue
        x,y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print( " Введите верные координаты")
            continue

        if field[x][y] != " ":
            print(" Клетка занята!")
            continue

        return x,y


#4. Выигрышные комбинации:
def win_cond():
    symb = []
    w_cords = (((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)),((0,0),(1,1),(2,2)),((0,2),(1,1),(2,0)))
    for cords in w_cords:
        for c in cords:
            symb.append(field[c[0]][c[1]])
        if symb == ["X","X","X"]:
            print( "Выиграл крестик!")
            return True
        if symb == ["0","0","0"]:
            print("Выиграл нолик!")
            return True
        if len(symb) == 3:
            symb.clear()
# 5. Приветствие.
def greeting():
    print("----------------------")
    print("  Приветствую вас")
    print("В игре крестики-нолики")
    print("----------------------")


# 6. Игровой цикл программы.
num = 0
greeting()
while True:
    show()
    num += 1
    if num % 2 ==  1:
        print('Ходит крестик:')
    else:
        print("Ходит нолик:")
    x,y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win_cond():
        break

    if num == 9:
        print("Ничья!")
        break

a = []
win = 77
for i in range(77): # создаем и заполняем
    a.append([0] * 77)

for i in range(77):
    for j in range(77):
        if i == 0 or j == 0:
            a[i][j] = -1            # нулевые строка и столбец неактивны, чтобы номер соотв кол-ву камней

# отмечаем победные за 1 ход
for i in range(77):
    for j in range(77):
        if i * 2 + j >= win or j * 2 + i >= win:
            a[i][j] = 1
# пробегаем массив от больших значений к маленьким
for i in range(76, 0, -1):
    for j in range(76, 0, -1):
        if a[i][j] == 0: # если клетка еще не заполнена
            # если есть выигрышный ход
            if a[i+1][j] % 2 == 0 or a[i*2][j] % 2 == 0 or a[i][j+1] % 2 == 0 or a[i][j*2] % 2 == 0:
                min_steps = 10000
                # ищем минимальную траекторию
                if a[i+1][j] % 2 == 0 and a[i+1][j] < min_steps:
                    min_steps = a[i+1][j]
                if a[i*2][j] % 2 == 0 and a[i*2][j] < min_steps:
                    min_steps = a[i*2][j]
                if a[i][j+1] % 2 == 0 and a[i][j+1] < min_steps:
                    min_steps = a[i][j+1]
                if a[i][j*2] % 2 == 0 and a[i][j*2] < min_steps:
                    min_steps = a[i][j*2]
                a[i][j] = min_steps + 1 # помечаем клетку выигрышной для 1 игрока (нечетной)
            # если все ходы проигрышные
            if a[i+1][j] % 2 == 1 and a[i*2][j] % 2 == 1 and a[i][j+1] % 2 == 1 and a[i][j*2] % 2 == 1:
                # выбираем максимальную траекторию, чтобы затянуть игру
                a[i][j] = max(a[i+1][j], a[i*2][j], a[i][j+1], a[i][j*2]) + 1

#for i in range(77):
#    print(a[i])
# выводим на экран нужную строку
print(a[7])

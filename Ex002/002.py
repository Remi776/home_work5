from random import randint as r
res = 2021
low = 1
high  = 28
def take_input(value, res):
    while True:
        player_count = int(input(f'{value + 1}-й игрок введите количество конфет: '))
        if player_count < low or player_count > high or player_count > res:
            print(f'Ошибка. Можно взять от {low} до {high}.')
        else:
            return player_count

value = bool(r(0, 1))
print(f'Игрок номер {value + 1} делает ход')
while res > 0:
    player_count = take_input(value, res)
    res -= player_count
    print(f'Осталось {res} конфет')
    if res == 0:
        print(f'Игрок {value + 1} победил!')
    value = not value
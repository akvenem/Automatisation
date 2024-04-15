m = int(input("Ввести номер месяца "))
def month_to_season(m):
    if m in range(1, 3) or m == 12:
        print("Зима")
    elif m in range(3, 6):
        print("Весна")
    elif m in range (6, 9):
        print("Лето")
    elif m in range (9, 12):
        print("Осень")
    else:
        print("Нет такого месяца")
month_to_season(m)

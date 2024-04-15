square = float(input("Введите сторону квадрата "))
if square != isinstance(square, int):
    import math
    square = math.ceil(square) #пришлось гуглить, не было такого в конспекте)
print("Площадь квадрата равна ", square*square)
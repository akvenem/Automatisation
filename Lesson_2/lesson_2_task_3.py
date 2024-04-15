import math
a = float(input("Введите сторону квадрата "))
def square(a):
    if a != isinstance(a, int):
        a = math.ceil(a) #пришлось гуглить, не было такого в конспекте)
        return a ** 2
print("Площадь квадрата равна ", square(a))
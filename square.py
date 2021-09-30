def rect_area(a, b) -> float:
    return a * b


def sq_area(a) -> float:
    return a * a


def tr_area(a, h) -> float:
    return 0.5 * a * h


def trap_area(a, b, h) -> float:
    return (a + b) * h * 0.5


def circ_area(r) -> float:
    return 3.14 * r * r


while True:
    print("Aby obliczyć pole prostokąta, wpisz 1")
    print("Aby obliczyć pole kwadratu, wpisz 2")
    print("Aby obliczyć pole trójkąta, wpisz 3")
    print("Aby obliczyć pole trapezu, wpisz 4")
    print("Aby obliczyć pole prostokąta, wpisz 5")
    print("Aby obliczyć pole koła, wpisz 6")
    print("Aby wyjść z programu, wpisz 0")

    option = input("Wybierz opcję: ")

    if option == "1":
        a = float(input("Podaj a: "))
        b = float(input("Podaj b: "))
        print(str(rect_area(a, b)))
    elif option == "2":
        a = float(input("Podaj a: "))
        print(str(sq_area(a)))
    elif option == "3":
        a = float(input("Podaj a: "))
        h = float(input("Podaj h: "))
        print(str(tr_area(a, h)))
    elif option == "4":
        a = float(input("Podaj a: "))
        b = float(input("Podaj b: "))
        h = float(input("Podaj h: "))
        print(str(trap_area(a, b, h)))
    elif option == "5":
        r = float(input("Podaj r: "))
        print(str(circ_area(r)))
    elif option == "0":
        break

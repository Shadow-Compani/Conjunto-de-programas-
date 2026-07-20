estacion = input("ingrerse un mes:")

match estacion:

    case "3"|"4"|"5":
        print("primavera")
    case "6"|"7"|"8":
        print("verano")
    case "9"|"10"|"11":
        print("otoño")
    case "12"|"1"|"2":
        print("invierno")
    case _:
        print("no")
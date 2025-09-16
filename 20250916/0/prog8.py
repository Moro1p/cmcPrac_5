match int(input()):
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case a if a % 2:
        print("odd")
    case a if not a % 2:
        print("even")

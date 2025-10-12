num = "4,3"
match num:
    case "2,3":
        print("The Addition of 2 and 3 is ",2+3)
    case "4,3":
        print("The subtraction of 4 and 3 is ",4-3)
    case "3*2":
        print("The multiplication of 3 and 2 is ",3*2)
    case "4,2":
        print("The xor of 4 and 2 is ",4^2)
    case _:
        print("invalid")
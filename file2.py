
def arthamatic_test(operator, param1, param2):
    print(f'Using argumnets are:', param1 , " & ",  param2)

    match operator:
        case "add":
            print(f' Add two numbers:', param1 + param2)
        case "subtract":
            if param1<param2:
                return print("Please check param2 value")
            print(f' Subtract two numbers:', param1 - param2)
        case "multiply":
            print(f' Multiply of two numbers:', param1 * param2)    
        case "division":
            if(param2 == 0):
                return print("please check arg2 should not be 0")
            print(f' Division of two numbers:', param1 / param2)
        case _:
            print("nothing matched")


arthamatic_test("subtract", 20, 40)                
def add(x,y):
    result = x + y
    return result

def subtract(x,y):
    result = x - y
    return result

def divide(x,y):
    result = x / y
    return result

def multiply(x,y):
    result = x * y
    return result

##########

x = int(input("x:"))
y = int(input("y:"))
z = input("operation:")

match(z):
    case "+" :
        print(add(x,y))
    case "-" :
        print(subtract(x,y))
    case "/" :
        print(divide(x,y))
    case "*":
        print(multiply(x,y))
    case _:
        print("Error, Please input a valid operation.")                

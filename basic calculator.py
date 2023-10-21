def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return("Not Divisible")
while True:
    print("SELECT THE OPERATION :")
    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    choice = input("Enter your Choice(1/2/3/4):")
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter your second number:"))
    if choice == "1":
        print ("Result :", add(num1,num2))
    elif choice == "2":
        print ("Result :", subtract(num1,num2))
    elif choice == "3":
        print ("Result :", multiply(num1,num2))
    elif choice == "4":
        print ("Result :", divide(num1,num2))
    else:
        print ("INVALID INPUT")
        
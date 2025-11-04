#Create a small calculator using functions (add, subtract, multiply, divide).
def add(a,b):
    return a+b
def subtract(a,b):
    return b-a
def multiply(a,b):
    return a*b
def divide(a,b):
    if(a==0):
        print("Division by zero error")
    else:
        return b/a
def remainder(a,b):
    if(a==0):
        print("Division by zero error")
    else:
        return b%a
def main():
    print("MENU \n1.ADD\n2.SUBTRACT\n3.MULTIPLY\n4.DIVISION\n5.REMAINDER\n6.EXIT\n")

    while(1):
        
        ch=int(input("Enter your choice: "))
        
        if(ch==1):
            a = int(input("Enter number: "))
            b=int(input("Enter number: "))
            print(add(a,b))
        elif(ch==2):
            a = int(input("Enter number: "))
            b=int(input("Enter number: "))
            print(subtract(a,b))
        elif(ch==3):
            a = int(input("Enter number: "))
            b=int(input("Enter number: "))
            print(multiply(a,b))
        elif(ch==4):
            a = int(input("Enter number: "))
            b=int(input("Enter number: "))
            print(divide(a,b))
        elif(ch==5):
            a = int(input("Enter number: "))
            b=int(input("Enter number: "))
            print(remainder(a,b))
        elif(ch==6):
            break;
        else:
            print("Invalid choice")
main()            
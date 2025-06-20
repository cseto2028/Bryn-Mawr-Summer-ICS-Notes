check= True 
while check == True: 
    print("Enter in your arithimetic operation: ")
    print("Multiplication") 
    print("Divison")
    print("Subtraction")
    print("Addition")
    print("Modular Division")
    option= input("Select your option above: ")
    if option == "multiplication":
        x= int(input("enter in num1"))
        y= int(input("enter in num2"))
        product= x * y 
        print(product)
    elif option == "division": 
        x= int(input("enter in num1"))
        y= int(input("enter in num2"))
        quotient= x//y 
        print(quotient)
    elif option== "subtraction": 
        x= int(input("enter in num1"))
        y= int(input("enter in num2"))
        subsum= x-y 
        print(subsum)
    elif option== "addition": 
        x= int(input("enter in num1")) 
        y= int(input("enter in num2"))
        sum= x + y 
        print(sum)
    elif option== "modular division": 
        x= int(input("enter in num1")) 
        y= int(input("enter in num2")) 
        modquotient= x%y 
        print(modquotient)
    elif option== "quit":
        check= False
    else: 
        print("unexpected error")




    
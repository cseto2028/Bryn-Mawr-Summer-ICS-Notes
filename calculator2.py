print("welcome to our calculator: ")
print("1. Addition") 
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")  
print("5. Modular Division") 
option= input("Enter the operation you would like to do: ")
if option == "addition" : 
    num1= int(input("enter num1"))
    num2= int(input("enter num2"))
    sum= num1 + num2 
    print(f"the sum of {num1} and {num2} is {sum}")
elif option == "subtraction": 
    num3= int(input("enter num3"))
    num4= int(input("enter num4"))
    sum1= num4 - num3 
    print(f"the sum of {num3} and {num4} is {sum1}")
elif option == "multiplication" : 
    num5= int(input("enter num5"))
    num6= int(input("enter num6"))
    product= num5 * num6 
    print(f"the product of {num5} and {num6} is {product}")
elif option == "division": 
    num7= int(input("enter num7"))
    num8= int(input("enter num8"))
    quotient= num8 // num7 
    print(f"the quotient of {num8} and {num7} is {quotient}")
elif option == "modular division": 
    num9= int(input("enter num9"))
    num10= int(input("enter num10"))
    quotient2= num10 % num9 
    print(f"the quotient of {num10} and {num9} is {quotient2}")
 


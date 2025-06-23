x= int(input(f"enter an integer"))
while x>= 2: 
    if x % 2 == 0: 
        print(f"this number is even. dividing by 2")
        x= x//2
        print(f"the hailstone's current height is {x}")
    else: 
        print(f"{x} is odd")
        x= x * 3 + 1
        print(f"the hailstone's current height is {x}")
        break


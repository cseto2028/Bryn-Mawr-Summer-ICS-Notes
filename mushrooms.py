mushrooms= []
check= True 
while check: 
    option= input(f"enter a mushroom weight")
    if option == "STOP":
        check = False 
    else: 
        option= int(option)
        if option < 1: 
         print(f"weight must be bigger than 0!") 
        else: 
            mushrooms.append(option)
big_mushrooms = 0 
small_mushrooms= 0 
medium_mushrooms= 0 
for size in mushrooms: 
    if size > 1000: 
       big_mushrooms += 1
    elif size >= 100 and size <= 1000: 
        medium_mushrooms += 1
    else: 
        small_mushrooms += 1
print(f"small mushrooms {small_mushrooms}: ")
print(f"medium mushrooms {medium_mushrooms}: ")
print(f"big mushrooms {big_mushrooms}")



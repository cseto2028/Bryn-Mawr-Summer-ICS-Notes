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
counts= {}
for size in mushrooms: 
    if size in counts: 
        counts[size] += 1
    else: 
        counts[size]= 1
for size in counts: 
    print(f"Size {size}: {counts[size]} mushrooms")



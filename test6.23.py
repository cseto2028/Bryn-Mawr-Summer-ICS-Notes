for i in range(10): 
    for j in range(4): 
        print(f"outer loop {i} inner loop {j}")
for i in range(1,13): 
    for j in range(1,13): 
        print(i * j, end = " ")
    print()
entrees= ["Steak", "Pasta", "Roasted Chicken", "Grilled Shrimp"]
sides= ["Breadsticks", "Fries", "Side Salad"]
print("welcome to olive garden")
for dish in entrees: 
    for side in sides: 
        print(f"main dish: {dish}, side dish: {side}")
for i in range(1,6): 
    for j in range(i): 
        print("*", end = " ")
    print()
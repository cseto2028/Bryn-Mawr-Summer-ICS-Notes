entrees= ["Steak", "Roast Chicken", "Pasta"]
price= [25, 19, 34]
for i in range(len(entrees)): 
    print(f"Entree: {entrees[i]} Price: {price[i]}")
entrees= {"Steak": 25, "Roast Chicken" : 19, "Pasta": 34}
print(entrees)
print(entrees["Steak"])
keys= list(entrees.keys())
print(keys)
entrees["Lobster"] = 60
print(entrees["Lobster"])
print(entrees)
mylist= [1,2,3,4]
mydict2= {}
mydict2["List"] = mylist 
print(mydict2)
print(mydict2["List"][1])
student= {"Name": "John Smith", "Grade Level": 9, "Email": "smithj@brynmawrschool.org"}
grades= {"English": 65, "Math": 100, "Social Studies": 85, "Biology": 70}
student["Grades"]= grades 
print(student["Grades"]["English"])
entrees.pop("Lobster")
print(entrees)
for item in entrees: 
    print(item)
for item in entrees: 
    print(entrees[item])
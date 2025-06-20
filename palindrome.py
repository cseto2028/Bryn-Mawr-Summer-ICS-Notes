word= input("enter your word: ")
copy= "" 
for char in word: 
    copy= (char + copy)
print(copy)
if word == copy: 
    print("this is a palindrome.")
else:  
    print("this is not a palindrome.")

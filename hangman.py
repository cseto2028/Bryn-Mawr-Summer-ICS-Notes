print("Welcome to Hangman!")
print("You have six incorrect tries to guess the word.")
word_list= [
    "hurl",
    "like",
    "mew",
    "insert",
    "pets",
    "wave",
    "same",
    "share",
    "speed",
    "rat",
    "push",
    "ill",
    "damp",
    "swallow",
    "pray",
    "join",
    "dine",
    "land",
    "spot",
    "scold",
    "hustle",
    "tramp",
    "colorful",
    "locket",
    "yam",
    "befall",
    "detach",
    "nip",
    "trust",
    "riddle",
    "begin",
    "offset",
    "slam",
    "wiry",
    "puny",
    "tap",
    "root",
    "reset",
    "differ",
    "cart",
    "trail",
    "way",
    "chain",
    "head",
    "word",
    "mind",
    "purify",
    "occupy",
    "big",
    "crime",
    "flimsy",
    "coat",
    "rub",
    "lick",
    "swing",
    "bed",
    "wet",
    "break",
    "slip",
    "pot",
    "wise",
    "ten",
    "chase",
    "bit",
    "flop",
    "pluck",
] 
import random 
def get_word(): 
    word= random.choice (word_list)
    return word
def checkLetter(letter, word): 
    for character in word: 
        if letter == character: 
            return True
    return False
def generateBlankWord(word):
    emptyword= []
    for letter in word: 
        emptyword.append("_")
    return emptyword 

def main():
    word= get_word()
    empty= generateBlankWord(word)
    print(empty)
    word_completion= "_" * len(word)
    guessed = False 
    guessed_letters= []
    guessed_words= []
    tries= 6
    hangman= ["     O    ",
              "    /","\\  ",
              "    |    ", 
              "    /","\\    "]
    guess= 0 
    check= True 
    while check == True: 
        option= input("Enter a letter as your guess: ")
        if checkLetter(option, word) == False: 
            guess += 1
        elif checkLetter(option, word) == True: 
            index = word.index(option)
            empty[index] = word [index]
            print(empty)
        if guess == 1: 
            print(hangman[0])
        elif guess == 2: 
            print(hangman[0])
            print(hangman[1])
        elif guess == 3: 
            print(hangman[0])
            print(f"{hangman[1]}{hangman[2]}")
        elif guess == 4: 
            print(hangman[0])
            print(f"{hangman[1]}{hangman[2]}")
            print(hangman[3])
        elif guess == 5: 
            print(hangman[0])
            print(f"{hangman[1]}{hangman[2]}")
            print(hangman[3])
            print(hangman[4])
        elif guess == 6: 
            print(hangman[0])
            print(f"{hangman[1]}{hangman[2]}")
            print(hangman[3])
            print(f"{hangman[4]}{hangman[5]}")
            print("Uh oh! You lost!")
            check = False 
        if empty == list(word): 
            print("Congrats, you won!")
            check = False 
            
    
main()
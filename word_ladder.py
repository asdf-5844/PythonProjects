initial_word=input("Enter a word: ")
def get_index(initial_word):
    index=int(input("Enter an index (-1 to quit): "))
    while index>len(initial_word)-1 or index<-1:
        print("Invalid index! Please enter a number between 0 and", len(word) - 1)
        index=int(input("Enter an index (-1 to quit): "))
    return index
def get_letter():
    letter=input("Enter a letter: ")
    while len(letter)!=1 or letter.isupper()==True:
        if len(letter)!=1:
            print("Must be exactly one character!")
        if letter.isupper()==True:
            print("Character must be a lowercase letter!")
        letter=input("Enter a letter: ")
    return letter
index=get_index(initial_word)
while index!=-1:
    letter=get_letter()
    list_word=list(initial_word)
    list_word[index]=letter
    initial_word = "".join(list_word)
    print(initial_word)
    index=get_index(initial_word)
    if index == -1:
        break

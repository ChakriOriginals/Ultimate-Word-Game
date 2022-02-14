import random 
import pandas as pd
import string

#importing the data set

print("WELCOME TO THE ULTIMATE WORD GAME !! \n Rules are : \n --> Enter any 5 letter word with CAPS ON!! \n --> If Correct alphabet is placed in the correct position then Code is 1 \n --> Else if correct alphabet at wrong position then the Code is 0. \n --> If the alphabet is not present in the word then the Code is -1 \n --> All the Best!   ")

Data = open("Game Dataset.txt", "r")
content = Data.read()
Data.close()
Mylist=[]
for x in content:
    Mylist = content.split(" ")

for i in range(len(Mylist)):
    Mylist[i] = Mylist[i].upper()

GameWord = random.choice(Mylist)
#print(GameWord)

GuessWord = input("Enter your guess word here: ")
print("You entered: ",GuessWord)

GameList=[]
for x in GameWord:
    GameList.extend(ord(n) for n in x)
del GameList[0]
#print("GameList : ",GameList)

GuessList=[]
for y in GuessWord:
    GuessList.extend(ord(m) for m in y)
#print("GuessList",GuessList)

WordLists = []
FinalList = [0,0,0,0,0]


def Game(GuessWord):
    FinalList = [0,0,0,0,0]
    WordLists = []
    GuessList=[]
    
    for y in GuessWord:
        GuessList.extend(ord(m) for m in y)

    for i in range(len(GameList)):
        for j in range(len(GuessList)):
            if GameList[i]==GuessList[j]:
                if i==j :
                    WordLists.append(1)
                else:
                    WordLists.append(0)
            
            if GameList[i]!=GuessList[j]:
                WordLists.append(-1)
         
    for i in range(len(FinalList)):
        FinalList[i]= max (WordLists[i],WordLists[i+5],WordLists[i+10],WordLists[i+15],WordLists[i+20])
        
    print("Code for your guess: ",FinalList)

    flag = False
    Nsum=0
    for i in range(len(FinalList)):
        Nsum+=FinalList[i]
        if Nsum==5:
            flag = True
        else:
            flag = False
        
    if flag == True :
        print("Wow! That's the correct answer")
    else:
        print("Sorry that's the wrong answer")

    PlayCode = input("Press 1 to get another chance \n or 0 to quit and know the answer :")
    PlayCode = int(PlayCode)

    if PlayCode == 0 :
        print("The Correct Answer is: ", GameWord )
        exit

    else:
        if PlayCode==1:
            NewGuess = input("Enter your guess word here: ")
            Game(NewGuess)
        else:
            exit
        
Game(GuessWord)        





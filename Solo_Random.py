import random
from Dice_idea_dictionary import *
Player_Score1 = 0
print('Welcome to the "Roll a Quiz" game!')
print('First of all, let us know who you are!')
player1 = input("You are the Player 1! Your name is ")
print('Okay, so let\'s begin our game!')
numberlist = []
while True:
    Question_Try1 = 1
    print(player1+','+" guess a roll")
    min = 1
    max = 6
    x = random.randint(min, max)
    y = random.randint(min, max)
    dice = (x+y)
    guess = int(input())
    if guess == int(dice):
        print("You guessed it right! Well done!")
        Player_Score1+=5
        Question_Try1 -=1
    else:
        print("You guessed it wrong. Maybe next time.")

    if Player_Score1 >=15:
        print("You won!")
        print(str(player1)+':'+str(Player_Score1))
        break

    if Question_Try1 == 1:
        print(player1+","+" answer the question.")
        QuestionNumber1 = 1
        QuestionNumber2 = 1
        QuestionNumber3 = 1
        loop1 = 1
        loop2 = 1
        loop3 = 1
        if QuestionNumber1 == 1:
            while loop1==1:
                x=random.randint(1,30)
                if x in numberlist:
                    loop1-=1
                else:
                    numberlist.append(x)
                    numberlist.sort()
                    list1 = []
                    list2 = []

                    list1.append('question')
                    list1.append(x)
                    QuestionString = ' '.join([str(elem) for elem in list1])
                    QuestionNumber = QuestionString.replace(" ", "") 
                    print(QuestionDictionary[QuestionNumber])
                    print("Choose the correct answer")
                    answer = input()

                    list2.append('answer')
                    list2.append(x)
                    answerString = ' '.join([str(elem) for elem in list2])
                    answerNumber = answerString.replace(" ", "") 
                    if answer in answerDictionary[answerNumber]:
                        print("Correct")
                        Player_Score1 +=1
                        loop1 -=1
                        QuestionNumber1 -=1
                    else:
                        print("Incorrect")
                        loop1-=1
                        QuestionNumber1 -=1

        if QuestionNumber1 == 1:
            while loop1==0:
                x=random.randint(1,30)
                if x in numberlist:
                    loop1+=1
                else:
                    numberlist.append(x)
                    numberlist.sort()
                    list1 = []
                    list2 = []

                    list1.append('question')
                    list1.append(x)
                    QuestionString = ' '.join([str(elem) for elem in list1])
                    QuestionNumber = QuestionString.replace(" ", "") 
                    print(QuestionDictionary[QuestionNumber])
                    print("Choose the correct answer")

                    answer = input()

                    list2.append('answer')
                    list2.append(x)
                    answerString = ' '.join([str(elem) for elem in list2])
                    answerNumber = answerString.replace(" ", "") 
                    if answer in answerDictionary[answerNumber]:
                        print("Correct")
                        Player_Score1 +=1
                        loop1 +=1
                        QuestionNumber1 -=1
                    else:
                        print("Incorrect")
                        loop1 +=1
                        QuestionNumber1 -=1
        
        if QuestionNumber2 ==1:
            while loop2==1:
                x=random.randint(31,60)
                if x in numberlist:
                    loop2-=1
                else:
                    numberlist.append(x)
                    numberlist.sort()
                    list1 = []
                    list2 = []

                    list1.append('question')
                    list1.append(x)
                    QuestionString = ' '.join([str(elem) for elem in list1])
                    QuestionNumber = QuestionString.replace(" ", "") 
                    print(QuestionDictionary[QuestionNumber])
                    print('Answer with "True" or "False"')

                    answer = input()

                    list2.append('answer')
                    list2.append(x)
                    answerString = ' '.join([str(elem) for elem in list2])
                    answerNumber = answerString.replace(" ", "") 
                    if answer in answerDictionary[answerNumber]:
                        print("Correct")
                        Player_Score1 +=1
                        QuestionNumber2 -= 1
                        loop2-=1
                    else:
                        print("Incorrect")
                        QuestionNumber2 -= 1
                        loop2-=1
               
        if QuestionNumber2 == 1:
            while loop2==0:
                x=random.randint(31,60)
                if x in numberlist:
                    loop2+=1
                else:
                    numberlist.append(x)
                    numberlist.sort()
                    list1 = []
                    list2 = []

                    list1.append('question')
                    list1.append(x)
                    QuestionString = ' '.join([str(elem) for elem in list1])
                    QuestionNumber = QuestionString.replace(" ", "") 
                    print(QuestionDictionary[QuestionNumber])
                    print('Answer with "True" or "False"')

                    answer = input()

                    list2.append('answer')
                    list2.append(x)
                    answerString = ' '.join([str(elem) for elem in list2])
                    answerNumber = answerString.replace(" ", "") 
                    if answer in answerDictionary[answerNumber]:
                        print("Correct")
                        Player_Score1 +=1
                        QuestionNumber2 -= 1
                        loop2+=1
                    else:
                        print("Incorrect")
                        QuestionNumber2 -= 1
                        loop2+=1
        
        if QuestionNumber3 == 1:
            while loop3==1:
                x=random.randint(61,90)
                if x in numberlist:
                    loop3-=1
                else:
                    numberlist.append(x)
                    numberlist.sort()
                    list1 = []
                    list2 = []

                    list1.append('question')
                    list1.append(x)
                    QuestionString = ' '.join([str(elem) for elem in list1])
                    QuestionNumber = QuestionString.replace(" ", "") 
                    print(QuestionDictionary[QuestionNumber])
                    

                    answer = input()

                    list2.append('answer')
                    list2.append(x)
                    answerString = ' '.join([str(elem) for elem in list2])
                    answerNumber = answerString.replace(" ", "") 
                    if answer in answerDictionary[answerNumber]:
                        print("Correct")
                        Player_Score1 +=2
                        Question_Try1 -= 1
                        QuestionNumber3 -= 1
                        loop3-=1
                    else:
                        print("Incorrect")
                        Question_Try1 -=1
                        QuestionNumber3 -= 1
                        loop3-=1
                
        if QuestionNumber3 == 1:
            while loop3==0:
                x=random.randint(61,90)
                if x in numberlist:
                    loop3+=1
                else:
                    numberlist.append(x)
                    numberlist.sort()
                    list1 = []
                    list2 = []

                    list1.append('question')
                    list1.append(x)
                    QuestionString = ' '.join([str(elem) for elem in list1])
                    QuestionNumber = QuestionString.replace(" ", "") 
                    print(QuestionDictionary[QuestionNumber])

                    answer = input()

                    list2.append('answer')
                    list2.append(x)
                    answerString = ' '.join([str(elem) for elem in list2])
                    answerNumber = answerString.replace(" ", "") 

                    if answer in answerDictionary[answerNumber]:
                        Player_Score1 +=2
                        Question_Try1 -= 1
                        QuestionNumber3 -= 1
                        loop3+=1
                    else:
                        print("Incorrect")
                        Question_Try1 -=1
                        QuestionNumber3 -= 1
                        loop3+=1
    if Player_Score1 >=15:
        print("You won!")
        print(str(player1)+':'+str(Player_Score1))
        break
import random
from Dice_idea_dictionary import *
Player_Score1 = 0
loop1=1
loop2=31
loop3=61
player1=input()
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
        print(str(player1)+':'+str(Player_Score1))
        break
    
    if Question_Try1 ==1:
        print(player1,"answer the quastions")
        list1 = []
        list2 = []
        x=loop1
        list1.append('question')
        list1.append(x)
        QuestionString = ' '.join([str(elem) for elem in list1])
        QuestionNumber =  QuestionString.replace(" ", "") 
        print(QuestionDictionary[QuestionNumber])
        print("Choose the correct answer")
        answer = input()

        list2.append('answer')
        list2.append(x)
        answerString = ' '.join([str(elem) for elem in list2])
        answerNumber = answerString.replace(" ", "") 
        if answer == answerDictionary[answerNumber]:
            print("Correct")
            Player_Score1 +=1
            loop1 += 1
        else:
            print("Incorrect")

        #player 1 question 2
        list3 = []
        list4 = []
        x=loop2
        list3.append('question')
        list3.append(x)
        QuestionString = ' '.join([str(elem) for elem in list3])
        QuestionNumber = QuestionString.replace(" ", "") 
        print(QuestionDictionary[QuestionNumber])
        print('Answer with "True" or "False"')
        answer = input()

        list4.append('answer')
        list4.append(x)
        answerString = ' '.join([str(elem) for elem in list4])
        answerNumber = answerString.replace(" ", "") 
        if answer == answerDictionary[answerNumber]:
            print("Correct")
            Player_Score1 +=1
            loop2+=1
        else:
            print("Incorrect")
                
        #player 1 question 3
        list5 = []
        list6 = []
        x=loop3
        list5.append('question')
        list5.append(x)
        QuestionString = ' '.join([str(elem) for elem in list5])
        QuestionNumber = QuestionString.replace(" ", "") 
        print(QuestionDictionary[QuestionNumber])

        answer = input()

        list6.append('answer')
        list6.append(x)
        answerString = ' '.join([str(elem) for elem in list6])
        answerNumber = answerString.replace(" ", "") 
        if answer == answerDictionary[answerNumber]:
            print("Correct")
            Player_Score1 +=2
            Question_Try1-=1
            loop3+=1
        else:
            print("Incorrect")
            Question_Try1-=1

        if Player_Score1 >=15:
            print(str(player1)+':'+str(Player_Score1))
            break
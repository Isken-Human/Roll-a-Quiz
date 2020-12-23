import random
from Dice_idea_dictionary import*

#The beginning part
print('Welcome to the "Roll a Quiz" game!')
print('First of all, let us know who you are!')
player1 = input("You are the Player 1! Your name is ")
player2 = input("You are the Player 2! Your name is ")
player3 = input("You are the Player 3! Your name is ")
print('Okay, so let\'s begin our game!')

#player scores
Player_Score1 = 0
Player_Score2 = 0
Player_Score3 = 0

#Starting point for questions
loop1 = 1
loop2 = 31
loop3 = 61
while True:
    #Counter of tries
    Dice_Try1 = 1
    Dice_Try2 = 1
    Dice_Try3 = 1

    #player question skip
    Question_Try1 = 1
    Question_Try2 = 1
    Question_Try3 = 1
    while Dice_Try3 == 1:
        #Player1 guess
        if Dice_Try1 ==1:
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
                Dice_Try1 -=1
                Question_Try1 -=1
            else:
                print("You guessed it wrong. Maybe next time.")
                Dice_Try1 -=1
        #Player2 guess
        if Dice_Try2 ==1:
            print(player2 + ',' + " guess a roll")
            min = 1
            max = 6
            x = random.randint(min, max)
            y = random.randint(min, max)
            dice = (x+y)
            guess = int(input())
            if guess == int(dice):
                print("You guessed it right! Well done!")
                Player_Score2+=5  
                Dice_Try2 -=1 
                Question_Try2 -=1
            else:
                print("You guessed it wrong. Maybe next time.")
                Dice_Try2 -=1     
        #Player3 guess
        if Dice_Try3 ==1:
            print(player3 + ',' + " guess a roll")
            min = 1
            max = 6
            x = random.randint(min, max)
            y = random.randint(min, max)
            dice = (x+y)
            guess = int(input())
            if guess == int(dice):
                print("You guessed it right! Well done!")
                Player_Score3+=5
                Dice_Try3 -=1
                Question_Try3 -=1
            else:
                print("You guessed it wrong. Maybe next time.")
                Dice_Try3 -=1
    
    #Ending the game when the score is bigger or equal 15
    if Player_Score1 >=15:
        if Player_Score1 == Player_Score2 and Player_Score1 == Player_Score3:
            print(player1+', '+player2+', '+player3+', '+"you all did well!")
            print(str(player1)+':'+str(Player_Score1))
            print(str(player2)+':'+str(Player_Score2))  
            print(str(player3)+':'+str(Player_Score3))
            break
        elif Player_Score1 == Player_Score2:
            print("Winners are",player1+" and "+player2)
            print(str(player1)+':'+str(Player_Score1))
            print(str(player2)+':'+str(Player_Score2))  
            print(str(player3)+':'+str(Player_Score3))
            break
        elif Player_Score1 == Player_Score3:
            print("Winners are",player1+" and "+player3)
            print(str(player1)+':'+str(Player_Score1))
            print(str(player3)+':'+str(Player_Score3))
            print(str(player2)+':'+str(Player_Score2))
            break
        print("Winner is",player1)
        print(str(player1)+':'+str(Player_Score1))
        if Player_Score2>Player_Score3:
            print(str(player2)+':'+str(Player_Score2))  
            print(str(player3)+':'+str(Player_Score3))
        else:
            print(str(player3)+':'+str(Player_Score3))
            print(str(player2)+':'+str(Player_Score2)) 
        break     
    if Player_Score2 >=15:
        if Player_Score2 == Player_Score3:
            print("Winners are",player2+" and "+player3)
            print(str(player2)+':'+str(Player_Score2))
            print(str(player3)+':'+str(Player_Score3))
            print(str(player1)+':'+str(Player_Score1))
            break
        print("Winner is",player2)
        print(str(player2)+':'+str(Player_Score2))  
        if Player_Score1>Player_Score3:
            print(str(player1)+':'+str(Player_Score1))
            print(str(player3)+':'+str(Player_Score3)) 
        else:
            print(str(player3)+':'+str(Player_Score3)) 
            print(str(player1)+':'+str(Player_Score1))
        break 
    if Player_Score3 >=15:
        print("Winner is",player3)
        print(str(player3)+':'+str(Player_Score3))
        if Player_Score1>Player_Score2:
            print(str(player1)+':'+str(Player_Score1))
            print(str(player2)+':'+str(Player_Score2)) 
        else:
            print(str(player2)+':'+str(Player_Score2)) 
            print(str(player1)+':'+str(Player_Score1))
        break        
    
    #Answering questions part
    while Question_Try1 == 1 or Question_Try2 == 1 or Question_Try3 ==1:
        #player 1 answers
        if Question_Try1 ==1:
            #player 1 Question 1
            print(player1+","+" answer the question.")
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
            if answer in answerDictionary[answerNumber]:
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
            if answer in answerDictionary[answerNumber]:
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
            if answer in answerDictionary[answerNumber]:
                    print("Correct")
                    Player_Score1 +=2
                    Question_Try1-=1
                    loop3+=1
            else:
                    print("Incorrect")
                    Question_Try1-=1
        
        #player 2 answers
        if Question_Try2 == 1:
            #player 2 question 1
            print(player2+","+" answer the question.")
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
            if answer in answerDictionary[answerNumber]:
                    print("Correct")
                    Player_Score2 +=1
                    loop1 += 1
            else:
                    print("Incorrect")

            #player 2 question 2
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
            if answer in answerDictionary[answerNumber]:
                    print("Correct")
                    Player_Score2 +=1
                    loop2+=1
            else:
                    print("Incorrect")
            
            #player 2 question 3
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
            if answer in answerDictionary[answerNumber]:
                    print("Correct")
                    Player_Score2 +=2
                    Question_Try2-=1
                    loop3+=1
            else:
                    print("Incorrect")
                    Question_Try2-=1
        
        #player 3 answers
        if Question_Try3 ==1:
                        #player 3 Question 1
            print(player3+","+" answer the question.")
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
            if answer in answerDictionary[answerNumber]:
                    print("Correct")
                    Player_Score3 +=1
                    loop1 += 1
            else:
                    print("Incorrect")
                    loop1 += 1

            #player 3 question 2
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
            if answer in answerDictionary[answerNumber]:
                    print("Correct")
                    Player_Score3 +=1
                    loop2+=1
            else:
                    print("Incorrect")
                    loop2+=1
            
            #player 3 question 3
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
            if answer in answerDictionary[answerNumber]:
                    print("Correct")
                    Player_Score3 +=2
                    Question_Try3-=1
                    loop3+=1
            else:
                    print("Incorrect")
                    Question_Try3-=1
                    loop3 +=1
    
    #Printing the result of the game
    print(str(player1)+':'+str(Player_Score1))
    print(str(player2)+':'+str(Player_Score2))  
    print(str(player3)+':'+str(Player_Score3))

    #Ending the game when the score is bigger or equal 15
    if Player_Score1 >=15:
        if Player_Score1 == Player_Score2 and Player_Score1 == Player_Score3:
            print(player1+', '+player2+', '+player3+', '+"you all did well!")
            print(str(player1)+':'+str(Player_Score1))
            print(str(player2)+':'+str(Player_Score2))  
            print(str(player3)+':'+str(Player_Score3))
            break
        elif Player_Score1 == Player_Score2:
            print("Winners are",player1+" and "+player2)
            print(str(player1)+':'+str(Player_Score1))
            print(str(player2)+':'+str(Player_Score2))  
            print(str(player3)+':'+str(Player_Score3))
            break
        elif Player_Score1 == Player_Score3:
            print("Winners are",player1+" and "+player3)
            print(str(player1)+':'+str(Player_Score1))
            print(str(player3)+':'+str(Player_Score3))
            print(str(player2)+':'+str(Player_Score2))
            break
        print("Winner is",player1)
        print(str(player1)+':'+str(Player_Score1))
        if Player_Score2>Player_Score3:
            print(str(player2)+':'+str(Player_Score2))  
            print(str(player3)+':'+str(Player_Score3))
        else:
            print(str(player3)+':'+str(Player_Score3))
            print(str(player2)+':'+str(Player_Score2)) 
        break     
    if Player_Score2 >=15:
        if Player_Score2 == Player_Score3:
            print("Winners are",player2+" and "+player3)
            print(str(player2)+':'+str(Player_Score2))
            print(str(player3)+':'+str(Player_Score3))
            print(str(player1)+':'+str(Player_Score1))
            break
        print("Winner is",player2)
        print(str(player2)+':'+str(Player_Score2))  
        if Player_Score1>Player_Score3:
            print(str(player1)+':'+str(Player_Score1))
            print(str(player3)+':'+str(Player_Score3)) 
        else:
            print(str(player3)+':'+str(Player_Score3)) 
            print(str(player1)+':'+str(Player_Score1))
        break 
    if Player_Score3 >=15:
        print("Winner is",player3)
        print(str(player3)+':'+str(Player_Score3))
        if Player_Score1>Player_Score2:
            print(str(player1)+':'+str(Player_Score1))
            print(str(player2)+':'+str(Player_Score2)) 
        else:
            print(str(player2)+':'+str(Player_Score2)) 
            print(str(player1)+':'+str(Player_Score1))
        break  
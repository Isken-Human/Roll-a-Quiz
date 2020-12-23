import random
from Dice_idea_dictionary import *

#The beginning part
print('Welcome to the "Roll a Quiz" game!')
print('First of all, let us know who you are!')
player1 = input("You are the Player 1! Your name is ")
player2 = input("You are the Player 2! Your name is ")
player3 = input("You are the Player 3! Your name is ")
print('Okay, so let\'s begin our game!')

Player_Score1 = 0
Player_Score2 = 0
Player_Score3 = 0

numberlist=[]
numberlist2=[]
numberlist3=[]
while True:
    Dice_Try1 = 1
    Dice_Try2 = 1
    Dice_Try3 = 1

    Question_Try1 = 1
    Question_Try2 = 1
    Question_Try3 = 1

    while Dice_Try1 == 1 or Dice_Try2 == 1 or Dice_Try3 ==1:
        Dice_Print1 = 1
        if Dice_Try1 == 1 and Dice_Print1 == 1:
            print(player1+','+" guess a roll")
            Dice_Print1 -= 1
        elif Dice_Try2 == 1 and Dice_Print1 == 1:
            print(player2+','+" guess a roll")
            Dice_Print1 -= 1
        elif Dice_Try3 == 1 and Dice_Print1 == 1:
            print(player3+','+" guess a roll")
            Dice_Print1 -= 1
        min = 1
        max = 6
        x = random.randint(min, max)
        y = random.randint(min, max)
        dice = (x+y)
        guess = int(input())
        if guess == int(dice):
            print("You guessed it right! Well done!")
            if Dice_Try1 == 1:
                Player_Score1 +=5
                Dice_Try1 -=1
                Question_Try1 -=1
            elif Dice_Try2 == 1:
                Player_Score2 +=5
                Dice_Try2 -=1
                Question_Try2 -=1
            elif Dice_Try3 == 1:
                Player_Score3 +=5
                Dice_Try3 -=1
                Question_Try3 -=1
        else:
            print("You guessed it wrong. Maybe next time.")
            if Dice_Try1 == 1:
                Dice_Try1 -= 1
            elif Dice_Try2 == 1:
                Dice_Try2 -= 1
            elif Dice_Try3 == 1:
                Dice_Try3 -= 1

    if Player_Score1 >= 15 or Player_Score2 >= 15 or Player_Score3 >= 15:
        if Player_Score1 > Player_Score2 and Player_Score1 >  Player_Score3:
            print("Winner is",player1)
            print(str(player1)+':'+str(Player_Score1))
            if Player_Score2>Player_Score3:
                print(str(player2)+':'+str(Player_Score2))  
                print(str(player3)+':'+str(Player_Score3))
            else:
                print(str(player3)+':'+str(Player_Score3))
                print(str(player2)+':'+str(Player_Score2)) 
            break     
        if Player_Score2 > Player_Score1 and Player_Score2 > Player_Score3:
            print("Winner is",player2)
            print(str(player2)+':'+str(Player_Score2))  
            if Player_Score1>Player_Score3:
                print(str(player1)+':'+str(Player_Score1))
                print(str(player3)+':'+str(Player_Score3)) 
            else:
                print(str(player3)+':'+str(Player_Score3)) 
                print(str(player1)+':'+str(Player_Score1))
            break 
        if Player_Score3 > Player_Score1 and Player_Score3 > Player_Score2:
            print("Winner is",player3)
            print(str(player3)+':'+str(Player_Score3))
            if Player_Score1>Player_Score2:
                print(str(player1)+':'+str(Player_Score1))
                print(str(player2)+':'+str(Player_Score2)) 
            else:
                print(str(player2)+':'+str(Player_Score2)) 
                print(str(player1)+':'+str(Player_Score1))
            break
        if Player_Score1 == Player_Score2 and Player_Score1 == Player_Score3:
                print(player1+', '+player2+', '+player3+', '+"you all did well!")
                print(str(player1)+':'+str(Player_Score1))
                print(str(player2)+':'+str(Player_Score2))  
                print(str(player3)+':'+str(Player_Score3))
                break
        if Player_Score1 == Player_Score2:
            print("Winners are",player1+" and "+player2)
            print(str(player1)+':'+str(Player_Score1))
            print(str(player2)+':'+str(Player_Score2))  
            print(str(player3)+':'+str(Player_Score3))
            break
        if Player_Score1 == Player_Score3:
            print("Winners are",player1+" and "+player3)
            print(str(player1)+':'+str(Player_Score1))
            print(str(player3)+':'+str(Player_Score3))
            print(str(player2)+':'+str(Player_Score2))
            break
        if Player_Score2 == Player_Score3:
            print("Winners are",player2+" and "+player3)
            print(str(player2)+':'+str(Player_Score2))
            print(str(player3)+':'+str(Player_Score3))
            print(str(player1)+':'+str(Player_Score1))
            break
        
    while Question_Try1 == 1 or Question_Try2 == 1 or Question_Try3 ==1:
        QuestionNumber1 = 1
        QuestionNumber2 = 1
        QuestionNumber3 = 1
        QuestionLoop1 = 1
        QuestionLoop2 = 1
        QuestionLoop3 = 1
        loop1 = 1
        loop2 = 1
        loop3 = 1
        while QuestionLoop1 == 1:
            if QuestionNumber1 == 1:
                while loop1==1:
                    x=random.randint(1,30)
                    if x in numberlist:
                        loop1-=1
                    else:
                        Question_Print = 1
                        if Question_Print == 1 and Question_Try1 == 1:
                            print(player1+","+"answer the question")
                        elif Question_Print == 1 and Question_Try2 == 1:
                            print(player2+","+"answer the question")
                        elif Question_Print == 1 and Question_Try3 == 1:
                            print(player3+","+"answer the question")
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
                            if Question_Try1 == 1:
                                Player_Score1 +=1
                                QuestionNumber1 -= 1
                                QuestionLoop1 -= 1
                                loop1-=1
                            elif Question_Try2 == 1:
                                Player_Score2 += 1
                                QuestionNumber1 -= 1
                                QuestionLoop1 -= 1
                                loop1-=1
                            elif Question_Try3 == 1:
                                Player_Score3 +=1
                                QuestionNumber1 -= 1
                                QuestionLoop1 -= 1
                                loop1-=1
                        else:
                            print("Incorrect")
                            if Question_Try1 == 1:
                                QuestionNumber1 -= 1
                                QuestionLoop1 -= 1
                                loop1-=1
                            elif Question_Try2 == 1:
                                QuestionNumber1 -= 1
                                QuestionLoop1 -= 1
                                loop1-=1
                            elif Question_Try3 == 1:
                                QuestionNumber1 -= 1
                                QuestionLoop1 -= 1
                                loop1-=1
                            
            if QuestionNumber1 ==1:
                while loop1==0:
                    x=random.randint(1,30)
                    if x in numberlist:
                        loop1+=1
                    else:
                        Question_Print = 1
                        if Question_Print == 1 and Question_Try1 == 1:
                            print(player1+","+"answer the question")
                        elif Question_Print == 1 and Question_Try2 == 1:
                            print(player2+","+"answer the question")
                        elif Question_Print == 1 and Question_Try3 == 1:
                            print(player3+","+"answer the question")
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
                            if Question_Try1 == 1:
                                Player_Score1 +=1
                                QuestionNumber1 -= 1
                                QuestionLoop1 -= 1
                                loop1+=1
                            elif Question_Try2 == 1:
                                Player_Score2 += 1
                                QuestionNumber1 -= 1
                                QuestionLoop1 -= 1
                                loop1+=1
                            elif Question_Try3 == 1:
                                Player_Score3 +=1
                                QuestionNumber1 -= 1
                                QuestionLoop1 -= 1
                                loop1+=1
                        else:
                            print("Incorrect")
                            if Question_Try1 == 1:
                                QuestionNumber1 -= 1
                                QuestionLoop1 -= 1
                                loop1+=1
                            elif Question_Try2 == 1:
                                QuestionNumber1 -= 1
                                QuestionLoop1 -= 1
                                loop1+=1
                            elif Question_Try3 == 1:
                                QuestionNumber1 -= 1
                                QuestionLoop1 -= 1
                                loop1+=1
        
        while QuestionLoop2 == 1:
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
                            if Question_Try1 == 1:
                                Player_Score1 +=1
                                QuestionNumber2 -= 1
                                QuestionLoop2 -= 1
                                loop2-=1
                            elif Question_Try2 == 1:
                                Player_Score2 += 1
                                QuestionNumber2 -= 1
                                QuestionLoop2 -= 1
                                loop2-=1
                            elif Question_Try3 == 1:
                                Player_Score3 +=1
                                QuestionNumber2 -= 1
                                QuestionLoop2 -= 1
                                loop2-=1
                        else:
                            print("Incorrect")
                            if Question_Try1 == 1:
                                QuestionNumber2 -= 1
                                QuestionLoop2 -= 1
                                loop2-=1
                            elif Question_Try2 == 1:
                                QuestionNumber2 -= 1
                                QuestionLoop2 -= 1
                                loop2-=1
                            elif Question_Try3 == 1:
                                QuestionNumber2 -= 1
                                QuestionLoop2 -= 1
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
                            if Question_Try1 == 1:
                                Player_Score1 +=1
                                QuestionNumber2 -= 1
                                QuestionLoop2 -= 1
                                loop2+=1
                            elif Question_Try2 == 1:
                                Player_Score2 += 1
                                QuestionNumber2-= 1
                                QuestionLoop2 -= 1
                                loop2+=1
                            elif Question_Try3 == 1:
                                Player_Score3 +=1
                                QuestionNumber2 -= 1
                                QuestionLoop2 -= 1
                                loop2+=1
                        else:
                            print("Incorrect")
                            if Question_Try1 == 1:
                                QuestionNumber2 -= 1
                                QuestionLoop2 -= 1
                                loop2+=1
                            elif Question_Try2 == 1:
                                QuestionNumber2 -= 1
                                QuestionLoop2 -= 1
                                loop2+=1
                            elif Question_Try3 == 1:
                                QuestionNumber2 -= 1
                                QuestionLoop2 -= 1
                                loop2+=1
                            
        while QuestionLoop3 == 1:
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
                        print("Answer the question")

                        answer = input()

                        list2.append('answer')
                        list2.append(x)
                        answerString = ' '.join([str(elem) for elem in list2])
                        answerNumber = answerString.replace(" ", "") 
                        if answer in answerDictionary[answerNumber]:
                            print("Correct")
                            if Question_Try1 == 1:
                                Player_Score1 +=2
                                Question_Try1 -= 1
                                QuestionNumber3 -= 1
                                QuestionLoop3 -= 1
                                loop3-=1
                            elif Question_Try2 == 1:
                                Player_Score2 += 2
                                Question_Try2 -= 1
                                QuestionNumber3 -= 1
                                QuestionLoop3 -= 1
                                loop3-=1
                            elif Question_Try3 == 1:
                                Player_Score3 +=2
                                Question_Try3 -= 1
                                QuestionNumber3 -= 1
                                QuestionLoop3 -= 1
                                loop3-=1
                        else:
                            print("Incorrect")
                            if Question_Try1 == 1:
                                Question_Try1 -=1
                                QuestionNumber3 -= 1
                                QuestionLoop3 -= 1
                                loop3-=1
                            elif Question_Try2 == 1:
                                Question_Try2 -=1
                                QuestionNumber3 -= 1
                                QuestionLoop3 -= 1
                                loop3-=1
                            elif Question_Try3 == 1:
                                Question_Try3 -=1
                                QuestionNumber3 -= 1
                                QuestionLoop3 -= 1
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
                        print("Answer the question")

                        answer = input()

                        list2.append('answer')
                        list2.append(x)
                        answerString = ' '.join([str(elem) for elem in list2])
                        answerNumber = answerString.replace(" ", "") 

                        if answer in answerDictionary[answerNumber]: 
                            print("Correct")
                            if Question_Try1 == 1:
                                Player_Score1 +=2
                                Question_Try1 -= 1
                                QuestionNumber3 -= 1
                                QuestionLoop3 -= 1
                                loop3+=1
                            elif Question_Try2 == 1:
                                Player_Score2 += 2
                                Question_Try2 -= 1
                                QuestionNumber3 -= 1
                                QuestionLoop3 -= 1
                                loop3+=1
                            elif Question_Try3 == 1:
                                Player_Score3 +=2
                                Question_Try3 -= 1
                                QuestionNumber3 -= 1
                                QuestionLoop3 -= 1
                                loop3+=1
                        else:
                            print("Incorrect")
                            if Question_Try1 == 1:
                                Question_Try1 -=1
                                QuestionNumber3 -= 1
                                QuestionLoop3 -= 1
                                loop3+=1
                            elif Question_Try2 == 1:
                                Question_Try2 -=1
                                QuestionNumber3 -= 1
                                QuestionLoop3 -= 1
                                loop3+=1
                            elif Question_Try3 == 1:
                                Question_Try3 -=1
                                QuestionNumber3 -= 1
                                QuestionLoop3 -= 1
                                loop3+=1
    
    if Player_Score1 >= 15 or Player_Score2 >= 15 or Player_Score3 >= 15:
        if Player_Score1 > Player_Score2 and Player_Score1 >  Player_Score3:
            print("Winner is",player1)
            print(str(player1)+':'+str(Player_Score1))
            if Player_Score2>Player_Score3:
                print(str(player2)+':'+str(Player_Score2))  
                print(str(player3)+':'+str(Player_Score3))
            else:
                print(str(player3)+':'+str(Player_Score3))
                print(str(player2)+':'+str(Player_Score2)) 
            break     
        if Player_Score2 > Player_Score1 and Player_Score2 > Player_Score3:
            print("Winner is",player2)
            print(str(player2)+':'+str(Player_Score2))  
            if Player_Score1>Player_Score3:
                print(str(player1)+':'+str(Player_Score1))
                print(str(player3)+':'+str(Player_Score3)) 
            else:
                print(str(player3)+':'+str(Player_Score3)) 
                print(str(player1)+':'+str(Player_Score1))
            break 
        if Player_Score3 > Player_Score1 and Player_Score3 > Player_Score2:
            print("Winner is",player3)
            print(str(player3)+':'+str(Player_Score3))
            if Player_Score1>Player_Score2:
                print(str(player1)+':'+str(Player_Score1))
                print(str(player2)+':'+str(Player_Score2)) 
            else:
                print(str(player2)+':'+str(Player_Score2)) 
                print(str(player1)+':'+str(Player_Score1))
            break
        if Player_Score1 == Player_Score2 and Player_Score1 == Player_Score3:
                print(player1+', '+player2+', '+player3+', '+"you all did well!")
                print(str(player1)+':'+str(Player_Score1))
                print(str(player2)+':'+str(Player_Score2))  
                print(str(player3)+':'+str(Player_Score3))
                break
        if Player_Score1 == Player_Score2:
            print("Winners are",player1+" and "+player2)
            print(str(player1)+':'+str(Player_Score1))
            print(str(player2)+':'+str(Player_Score2))  
            print(str(player3)+':'+str(Player_Score3))
            break
        if Player_Score1 == Player_Score3:
            print("Winners are",player1+" and "+player3)
            print(str(player1)+':'+str(Player_Score1))
            print(str(player3)+':'+str(Player_Score3))
            print(str(player2)+':'+str(Player_Score2))
            break
        if Player_Score2 == Player_Score3:
            print("Winners are",player2+" and "+player3)
            print(str(player2)+':'+str(Player_Score2))
            print(str(player3)+':'+str(Player_Score3))
            print(str(player1)+':'+str(Player_Score1))
            break
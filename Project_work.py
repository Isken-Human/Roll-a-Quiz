print("Choose between normal, random, solo or solo random.")
loop=1
while True:
    q=input()
    while loop==1:
        if q == "random":
            import Randomly_v2
            loop-=1         
        elif q=="normal":
            import In_Order 
            loop-=1
        elif q == "solo":
            import In_order_single
            loop-=1
        elif q == "solo random":
            import Solo_Random
            loop-=1
        else:
            print("Your choice is invalid!")
            loop-=1

    q2=input()
    while loop==0:
        if q2 == "random":
            import Randomly_v2
            loop+=1         
        elif q2=="normal":
            import In_Order 
            loop+=1
        elif q2 == "solo":
            import In_order_single
            loop+=1
        elif q2 == "solo random":
            import Solo_Random
            loop+=1   
        else:
            print("Your choice is invalid!")
            loop+=1

            
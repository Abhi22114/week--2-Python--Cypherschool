# Modify Number Gusseing game in python  

# winning_number=60
# guess=1
# number=int(input("guess a number between 1 and 100 : "))
# game_over=False

# while not game_over:
    # if number==winning_number:
        # print(f"you win , and you guessed this number in {guess} times ")
        # game_over=True
    # else:
        

        # if number < winning_number:
            # print("too low")
        #    guess+=1          
            #number =int(input("guess again :"))  #----> if we don't use this even  it will give clear rsults    (17,18)
        # else:
            # print("too high")   
        # guess+=1
        # number=int(input("guess again : "))


   
   
   
    #    DRY  ->>>don't repeat yourself

    #For selecting the number randomly we use random module (in built method)


import random 
winning_number =random.randint(1,100)
guess=1
number=int(input("guess a number between 1 and 100 : "))
game_over=False

while not game_over:
    if number==winning_number:
        print(f"you win , and you guessed this number in {guess} times ")
        game_over=True
    else:
        

        if number < winning_number:
            print("too low")
    
        else:
            print("too high")   
        guess+=1
        number=int(input("guess again : "))
import random
i = 0
play_again = True
check_int = True
while play_again is True:
    while i < 11 and play_again is True:
        check_int = False
        cor_reply = False
        if i == 0:
            gen_num = random.randint(1,99)
            print(gen_num)
            input_num  = (input(f"Enter your guess ({10-i}/10 guesses left ) : "))
            if input_num.isdigit() is True:
                in_num = int(input_num)
                if in_num > gen_num:
                    print("Lower number please!")
                    i += 1
                elif in_num < gen_num:
                    print("Higher number please!")
                    i += 1
                else:
                    while cor_reply is False:
                        reply= input(f"You guessed it correctly with {i} wrong guesses! Do you want to play again ? [Y/N] : ")
                        i = 0
                        if reply.upper() == "N":
                            print("Thanks!")
                            play_again = False
                            cor_reply = True
                        elif reply.upper() == "Y":
                            play_again = True
                            cor_reply = True
                        else:
                            print("invalid Input. Please try again")
                            cor_reply = False
            else:
                print("The input must be an integer")

    else:
        while cor_reply is False:
            reply= input(f"You have exhausted all your attempts. The number was {gen_num}. Do you want to play again ? [Y/N] : ")
            i = 0
            if reply.upper() == "N":
                print("Thanks!")
                play_again = False
                cor_reply = True
            elif reply.upper() == "Y":
                play_again = True
                cor_reply = True
            else:
                print("Ivalid input. Please try again")
                cor_reply = False



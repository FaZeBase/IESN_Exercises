import random
import time

def exit_program () :
    print("Have a nice day !")
def joke() :
    joke_nb = random.randint(0, 2)

    if joke_nb == 0 :
        print("Never trust an atom...\nThey make up everything! ")
    elif joke_nb == 1 :
        print("Why can't you hear a pterodactyl go to the bathroom ?\nThe 'p' is silent.") 
    elif joke_nb == 2 :
        print("What did the egg say to the boiling water ?\nIt'll be a minute before I get hard. I just got laid by a chick. ")
    else :
        print("There is a problem with this bot !\nPlease cpost an issue on Github")
def guessing_game() :
    nb_secret = random.randint(0, 420)
    nb_input = int(input("Number :"))
    while nb_secret != nb_input :    
        if nb_secret > nb_input :
            print("Too small")
        else :
            print("Too big")
        nb_input = int(input("Number :"))

    print("You won")
def countdown () :
    sec_countdown = int(input("The number of seconds to countdown :"))
    while sec_countdown > 0 :
        print(sec_countdown)
        time.sleep(1)
        sec_countdown -= 1
    print("Done")

input_main = input("What do you want me to do ? :")
if input_main == "x" :
    exit_program()
elif input_main == "j" :
    joke()
elif input_main == "g" :
    guessing_game()
elif input_main == "c" :
    countdown()
else :
    input_main = input("What do you want me to do ? :")

import time
def ticking_clock(secondes) :
    while secondes > 0 :
        if secondes % 2 == 0 :
            print("tic")
        else :
            print("tac")
        time.sleep(1)
        secondes -= 1
ticking_clock(50)

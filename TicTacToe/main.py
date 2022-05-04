#main script

import utils
import time

def main():

    NAME = "MAYCO"
    player_id = utils.register(NAME) 
    print (player_id)


    my_turn = utils.is_my_turn(player_id)

    while not my_turn:
        time.sleep(3)
        my_turn = utils.is_my_turn(player_id)


    print("its my turn, game continue...")

    print(my_turn)



if __name__ == "__main__":
    main()
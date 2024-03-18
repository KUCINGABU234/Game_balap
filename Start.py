from tqdm 
import tqdm
import time 
import os
import time
import random

for i in tqdm(range(10), desc="Loading", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]"):
    time.sleep(0.5) 

def clear_screen():
    os.system('clear')

def display_intro():
    clear_screen()
    print("welcome to my simple game")
    input("Press enter to start the game...")
    clear_screen()

def race():
    distance = 50
    player_position = 1
    computer_position = 1
    
    while player_position < distance and computer_position < distance:
        clear_screen()
        print("go go go!")
        print("Distance:", "-" * distance)
        print("Player:", " " * (player_position - 1) + "P")
        print("computer:", " " * (computer_position - 1) + "C")
        
        time.sleep(0.2)
        
        player_move = random.randint(1, 3)
        computer_move = random.randint(1, 3)
        
        player_position += player_move
        computer_position += computer_move
    
    clear_screen()
    if player_position >= distance:
        print("you win!")
    else:
        print("you lose!")

def main():
    display_intro()
    race()

if __name__ == "__main__":
    main()

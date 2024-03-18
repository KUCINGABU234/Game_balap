import os
import time
import random
from tqdm import tqdm

def clear_screen():
    os.system('clear')

def countdown():
    for i in tqdm(range(10, 0, -1), desc="Starting", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]"):
        time.sleep(0.8)
    clear_screen()

def display_intro():
    clear_screen()
    print("Welcome to my simple game")
    input("Press enter to start the game...")
    countdown()  # Menambahkan countdown sebelum memulai permainan

def race():
    distance = 50
    player_position = 1
    computer_position = 1

    while player_position < distance and computer_position < distance:
        clear_screen()
        print("Go go go!")
        print("Distance:", "-" * distance)
        print("Player:", " " * (player_position - 1) + "P")
        print("Computer:", " " * (computer_position - 1) + "C")

        time.sleep(0.2)

        player_move = random.randint(1, 3)
        computer_move = random.randint(1, 3)

        player_position += player_move
        computer_position += computer_move

    clear_screen()
    if player_position >= distance:
        print("You win!")
    else:
        print("You lose!")

def main():
    display_intro()
    race()

if __name__ == "__main__":
    main()
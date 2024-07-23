def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. There are paths to the left and right.")
    choice = input("Do you want to go left or right? (left/right) ").strip().lower()
    if choice == "left":
        go_left()
    elif choice == "right":
        go_right()
    else:
        print("Invalid choice. Please choose again.")
        start_game()

def go_left():
    print("You walk down the left path and encounter a friendly elf.")
    choice = input("Do you want to talk to the elf or ignore the elf? (talk/ignore) ").strip().lower()
    if choice == "talk":
        talk_to_elf()
    elif choice == "ignore":
        ignore_elf()
    else:
        print("Invalid choice. Please choose again.")
        go_left()

def go_right():
    print("You walk down the right path and fall into a trap.")
    choice = input("Do you want to try to escape or call for help? (escape/help) ").strip().lower()
    if choice == "escape":
        try_to_escape()
    elif choice == "help":
        call_for_help()
    else:
        print("Invalid choice. Please choose again.")
        go_right()

def talk_to_elf():
    print("The elf gives you a magical sword and tells you about a hidden treasure.")
    choice = input("Do you want to search for the treasure or continue on your way? (search/continue) ").strip().lower()
    if choice == "search":
        search_for_treasure()
    elif choice == "continue":
        continue_on_your_way()
    else:
        print("Invalid choice. Please choose again.")
        talk_to_elf()

def ignore_elf():
    print("You ignore the elf and continue walking. Unfortunately, you get lost in the forest.")
    choice = input("Do you want to try to find your way back or set up camp for the night? (find/camp) ").strip().lower()
    if choice == "find":
        find_way_back()
    elif choice == "camp":
        set_up_camp()
    else:
        print("Invalid choice. Please choose again.")
        ignore_elf()

def try_to_escape():
    print("You manage to escape the trap and find a hidden path.")
    choice = input("Do you want to follow the hidden path or go back to the main path? (follow/back) ").strip().lower()
    if choice == "follow":
        follow_hidden_path()
    elif choice == "back":
        go_back_to_main_path()
    else:
        print("Invalid choice. Please choose again.")
        try_to_escape()

def call_for_help():
    print("You call for help and a group of adventurers rescue you.")
    choice = input("Do you want to join the adventurers or continue on your own? (join/continue) ").strip().lower()
    if choice == "join":
        join_adventurers()
    elif choice == "continue":
        continue_on_your_own()
    else:
        print("Invalid choice. Please choose again.")
        call_for_help()

def search_for_treasure():
    print("You search for the treasure and find a chest filled with gold. You win!")
    play_again()

def continue_on_your_way():
    print("You continue on your way and safely reach a nearby village.")
    play_again()

def find_way_back():
    print("You find your way back to the main path and continue your journey.")
    play_again()

def set_up_camp():
    print("You set up camp for the night and are safe. In the morning, you find your way back.")
    play_again()

def follow_hidden_path():
    print("You follow the hidden path and discover a beautiful waterfall. You win!")
    play_again()

def go_back_to_main_path():
    print("You go back to the main path and continue your journey.")
    play_again()

def join_adventurers():
    print("You join the adventurers and together you find a hidden treasure. You win!")
    play_again()

def continue_on_your_own():
    print("You continue on your own and find a safe place to rest. You win!")
    play_again()

def play_again():
    choice = input("Do you want to play again? (yes/no) ").strip().lower()
    if choice == "yes":
        start_game()
    else:
        print("Thank you for playing! Goodbye.")

if _name_ == "_main_":
    start_game()

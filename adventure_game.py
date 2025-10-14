import time
import random


villains = ["dragon", "pirate", "wicked fairie", "trolls"]


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wild flowers.")
    print_pause(f"Rumor has it that a {villain} is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def field():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        response = input("(Please enter 1 or 2.)\n")

        if response == '1':
            house()
            break
        elif response == '2':
            cave()
            break


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door "
                f"opens and out steps a {villain}.")
    print_pause(f"Eep! This is the {villain}'s house!")
    print_pause(f"The {villain} attacks you!")
    print_pause("You feel a bit under-prepared for this, "
                "what with only having a tiny dagger.")
    while True:
        choice = input("Would you like to (1) fight or (2) run away?\n")
        if choice == '1':
            fight()
            break
        elif choice == '2':
            print_pause("You run back into the field. Luckily, "
                        "you don't seem to have been followed.\n")
            field()
            break


def fight():
    if 'sword' in item:
        print_pause(f"As the {villain} moves to attack, "
                    "you unsheath your new sword.")
        print_pause("The Sword of ogoroth shines brightly in your "
                    "hand as you brace yourself for the attack.")
        print_pause(f"But the {villain} takes one look at "
                    "your shiny new toy and runs away!")
        print_pause(f"You have rid the town of the {villain}. "
                    f"You are victorious!")
        play_again()
    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {villain}.")
        print_pause("You have been defeated!")
        play_again()


def cave():
    print_pause("You peer cautiously into the cave.")
    if 'sword' in item:
        print_pause("You've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.")
    else:
        print_pause("It turn out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
        item.append("sword")
    print_pause("You walk back out to the field.\n")
    field()


def play_again():
    while True:
        select = input("Would you like to play again? (y/n) \n").lower()
        if select == 'y':
            print_pause("Excellent! Restarting the game...")
            play_game()
            break
        elif select == 'n':
            print_pause("Thanks for playing! See you next time.")
            break


def play_game():
    global villain
    global item
    item = []
    villain = random.choice(villains)
    intro()
    field()


play_game()

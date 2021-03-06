import time
import random
items = []

villain = ['troll', 'crazy cook', 'pirate']
sel_villain = random.choice(villain)


def print_sleep(message_to_print):
    print(message_to_print)
    time.sleep(1)


def actions_cave_or_house(items):
    print_sleep("Enter 1 to knock on the door of the house.")
    print_sleep("Enter 2 to peer into the cave.")
    print_sleep("What would you like to do?")
    response = valid_input("Please enter 1 or 2.", "1", "2")
    if '1' in response:
        house(items)
        if '1' in response:
            fight(items)
        elif '2' in response:
            field(items)
    elif '2' in response:
        cave(items)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 == response:
            break
        elif option2 == response:
            break
        else:
            print_sleep("Sorry, I don't understand.")
    return response


def actions_fight_or_run(items):
    response2 = valid_input("Would you like to '1' fight or '2'"
                            " run away?", "1", "2")
    if '1' in response2:
        fight(items)
    elif '2' in response2:
        field(items)


def intro(items):
    print_sleep("You find yourself standing in an open field,")
    print_sleep("filled with grass and yellow wildflowers.")
    print_sleep("Rumor has it that a  " + sel_villain + " is somewhere")
    print_sleep("around here")
    print_sleep("and has been terrifying the nearby village.")
    print_sleep("In front of you is a house.")
    print_sleep("To your right is a dark cave.")
    print_sleep("In your hand you hold your trusty (but not very")
    print_sleep("effective) dagger.")
    actions_cave_or_house(items)


def play_again():
    print_sleep("Would you like to play again? ")
    response3 = valid_input("Please write 'yes' or 'no'", "yes", "no")
    if 'yes' in response3:
        play_game()
    elif 'no' in response3:
        print("It's been a pleasure, see you soon!")
        exit()


def fight(items):
    if 'sword' in items:
        print_sleep("As the  " + sel_villain + " moves to attack,")
        print_sleep("you unsheath your new sword.")
        print_sleep("The Sword of Ogoroth shines brightly in your")
        print_sleep("hand as you brace yourself for the attack.")
        print_sleep("But the  " + sel_villain + " takes one look at")
        print_sleep("your shiny new")
        print_sleep("toy and runs away!")
        print_sleep("You have rid the town of the  " + sel_villain + "!")
        print_sleep("You are victorious!")
        play_again()
        return None
    else:
        print_sleep("You do your best...")
        print_sleep("but your dagger is no match for ")
        print_sleep("the " + sel_villain + ".")
        print_sleep("You have been defeated!")
        play_again()


def cave(items):
    print_sleep("You peer cautiously into the cave")
    if 'sword' in items:
        print_sleep("You've been here before, and gotten all")
        print_sleep("the good stuff. It's just an empty cave now.")
        print_sleep("You walk back out to the field.")
        actions_cave_or_house(items)
    else:
        print_sleep("It turns out to be only a very small cave.")
        print_sleep("Your eye catches a glint of metal behind a rock.")
        print_sleep("You have found the magical Sword of Ogoroth!")
        print_sleep("You discard your silly old dagger and take the")
        print_sleep("sword with you.")
        print_sleep("You walk back out to the field.")
        items.append("sword")
        actions_cave_or_house(items)


def house(items):
    print_sleep("You approach the door of the house.")
    print_sleep("You are about to knock when the door opens and")
    print_sleep("out steps a  " + sel_villain + ".")
    print_sleep("Eep! This is the  " + sel_villain + "'s house!")
    print_sleep("The  " + sel_villain + " attacks you!")
    actions_fight_or_run(items)


def field(items):
    print_sleep("You run back into the field. Luckily,")
    print_sleep("you don't seem to have been followed.")
    actions_cave_or_house(items)


def play_game():
    global sel_villain
    sel_villain = random.choice(villain)
    items = []
    intro(items)
    actions_fight_or_run(items)
    actions_cave_or_house(items)


play_game()

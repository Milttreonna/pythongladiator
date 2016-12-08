from gladiator import Gladiator
# g = Gladiator
# g.attack()
# g.heal()
# g.isDead
# g.round
import random
import sys


def main():
    lowdam = random.randint(11, 20)
    highdam = random.randint(21, 30)
    print()
    print("•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*")
    print("""
 __                      __
/ _ | _  _|. _ |_ _  _  / _ . _| _
\__)|(_|(_||(_||_(_)|   \__)|| |_) """)
    print()
    print()
    print("•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*")
    print()
    gladiator_name = input("      What's player 1's name?")
    gladiator_name2 = input("      What's player 2's name?")
    print()
    gladiator2 = Gladiator(100, 0, lowdam, highdam, gladiator_name2)

    gladiator1 = Gladiator(100, 0, lowdam, highdam, gladiator_name)
    print("Hi", gladiator_name, "you will be player 1")
    print("Your rage starts at", gladiator1.rage)
    print("Your health is", gladiator1.health)

    print()
    print()
    print("Hi", gladiator2.name, "you will be player 2")
    print("Your rage starts at", gladiator2.rage)
    print("Your health is", gladiator2.health)
    print()
    print("•♥•♥•♥•♥•♥  Game is Starting  ♥•♥•♥•♥•♥•")
    print()
    print("          For attack, press (a)")
    print("           For heal, press (h)")
    print("          To give up, press (q)")
    print()
    while not gladiator1.isDead() and not gladiator2.isDead():
        print()
        print("Your health is", gladiator1.health)
        print(gladiator_name, "would you like to:")
        gladiator1.round(gladiator2)

        print()

        print("Your health is", gladiator2.health)
        print(gladiator_name2, "would you like to:")
        gladiator2.round(gladiator1)
        print()
        if gladiator2.health <= 0:
            print()
            print("     ", gladiator_name2, "your health is",
                  gladiator2.health)
            print("           ", gladiator_name, "wins!")
        elif gladiator1.health <= 0:
            print()
            print("     ", gladiator_name, "your health is", gladiator1.health)
            print("           ", gladiator_name2, "wins!")
        else:
            continue

        print()


if __name__ == '__main__':
    main()

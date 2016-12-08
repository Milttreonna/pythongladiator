import random
import sys


class Gladiator:
    def __init__(self, health, rage, lowdamage, highdamage, name):
        self.health = health
        self.rage = rage
        self.lowdamage = lowdamage
        self.highdamage = highdamage
        self.name = name

    def attack(self, other):
        hit = (random.randint(self.lowdamage, self.highdamage))
        if self.rage > random.randint(1, 100):
            hit *= 2
            self.rage = 0
        else:
            self.rage += 15
        other.health -= hit

    def heal(self):
        self.health += 5
        self.rage -= 10
        return None

    def isDead(self):
        if self.health <= 0:
            print("▬▬ι═══════ﺤ Game Over -═══════ι▬▬")
            sys.exit()
            return

    def round(self, other):

        fight = input("attack or heal?").lower().strip()
        if fight == "a":
            self.attack(other)
        elif fight == "h":
            self.heal()
        elif fight == "q":
            print()
            print("▬▬ι═══════ﺤ  Game Over  -═══════ι▬▬")
            print()
            print()
            print("    You gave up? What a disgrace ")
            print()
            print("             ( ︶︿︶)      ")
            print()
            print("       The other player wins")
            print()
            print()
            print("▬▬ι═══════ﺤ  Game Over  -═══════ι▬▬")
            sys.exit()
        else:
            print("You lost your turn")

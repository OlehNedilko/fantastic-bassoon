import random
import time

class Sigma():
    def __init__(self, health, heal, damage, ultimate):
        self.health = health
        self.heal = heal
        self.damage = damage
        self.ultimate = ultimate

SubZero = Sigma(200, 35, 25, 150)
Scorpion = Sigma(200, 35, 25, 135)
Scorpion_phrazes = random.randint(0, 7)
SubZero_phrazes = random.randint(0, 7)

while Scorpion.health > 0 and SubZero.health > 0:

    Scorpion_phrazes = random.randint(0, 7)
    SubZero_phrazes = random.randint(0, 7)


    if Scorpion_phrazes == 0:
        print("Scorpion: Get Over Here!")
        SubZero.health -= 25
        print(SubZero.health)
    if Scorpion_phrazes == 1:
        print("Scorpion: Come Here!")
        SubZero.health -= 25
        print(SubZero.health)
    if Scorpion_phrazes == 2:
        print("Scorpion: Get Over Here!")
        SubZero.health -= 25
        print(SubZero.health)
    if Scorpion_phrazes == 3:
        print("Scorpion: Come Here!")
        SubZero.health -= 25
        print(SubZero.health)
    if Scorpion_phrazes == 4:
        print("Scorpion: I wish...")
        time.sleep(1.5)
        print("Scorpion: For you to be dead!")
        SubZero.health -= 135
        print(SubZero.health)
    if Scorpion_phrazes == 5:
        print("Scorpion: Healing!")
        Scorpion.health += 35
        print(Scorpion.health)
    if Scorpion_phrazes == 6:
        print("Scorpion: Come Here!")
        SubZero.health -= 25
        print(SubZero.health)
    if Scorpion_phrazes == 7:
        print("Scorpion: Come Here!")
        SubZero.health -= 25
        print(SubZero.health)

    if SubZero_phrazes == 0:
        print("SubZero: Get Over Here!")
        Scorpion.health -= 25
        print(Scorpion.health)
    if SubZero_phrazes == 1:
        print("SubZero: Get Over Here!")
        Scorpion.health -= 25
        print(Scorpion.health)
    if SubZero_phrazes == 2:
        print("SubZero: Get Over Here!")
        Scorpion.health -= 25
        print(Scorpion.health)
    if SubZero_phrazes == 3:
        print("SubZero: Get Over Here!")
        Scorpion.health -= 25
        print(Scorpion.health)
    if SubZero_phrazes == 4:
        print("SubZero: Get Over Here!")
        Scorpion.health -= 25
        print(Scorpion.health)
    if SubZero_phrazes == 5:
        print("SubZero: Healing!")
        SubZero.health += 35
        print(SubZero.health)
    if SubZero_phrazes == 6:
        print("SubZero: I'm stronger than you think.")
        time.sleep(1.5)
        print("SubZero: I'm Sub-Zero, not Captain Cold.")
        time.sleep(1.5)
        print("SubZero: Ice Blow!!!")
        Scorpion.health -= 150
        print(Scorpion.health)
    if SubZero_phrazes == 7:
        print("SubZero: Get Over Here!")
        Scorpion.health -= 25
        print(Scorpion.health)
    
    time.sleep(2)
import random
import time

class dice():
    side = [1, 2, 3, 4, 5, 6]

    def throw(self):
        x = random.choice(self.side)
        print ("Dice result:", x)
        return (x)

class mainhero():
    hp = 10
    damage = 2
    dodge = 4
    acc = 2

    def __init__(self):
        print ("HERO: What inside this cave?")

    def death(self):
        if self.hp == 0 or self.hp < 0:
            print ("WASTED!")
            del self

    def attack(self, enemy, dice):
        if self.hp > 0 and enemy.hp > 0:
            actual_acc = self.acc + dice.throw()
            print ("SYSTEM: Player is trying to hit monster")
            time.sleep(2)
            if actual_acc > enemy.dodge:
                enemy.hp -= self.damage
                print ("SYSTEM: PLAYER HIT MONSTER ON:", self.damage, ". MONSTER HAS", enemy.hp, "HP LEFT")
                if enemy.hp == 0 or enemy.hp < 0:
                    enemy.death()
            else:
                time.sleep(2)
                print ("Player missed on emeny!")

class enemy1():
    hp = 6
    damage = 3
    dodge = 3
    acc = 3

    def __init__(self):
        print ("ENEMY: I will crash you!")

    def death(self):
        if self.hp == 0 or self.hp < 0:
            print ("ENEMY: Is over...")
            del self

    def attack(self, enemy, dice):
        if self.hp > 0 and enemy.hp > 0:
            actual_acc = self.acc + dice.throw()
            print ("SYSTEM: Monster is trying to hit player")
            time.sleep(2)
            if actual_acc > enemy.dodge:
                enemy.hp -= self.damage
                print ("SYSTEM: MONSTER HIT PLAYER ON:", self.damage, ". PLAYER HAS", enemy.hp, "HP LEFT")
                if enemy.hp == 0 or enemy.hp <0:
                    enemy.death()
            else:
                time.sleep(2)
                print ("Monster missed on player")


aaa = mainhero()
time.sleep(2)
bbb = enemy1()
ccc = dice()

while aaa.hp > 0 and bbb.hp > 0:
    aaa.attack(bbb, ccc)
    time.sleep(2)
    bbb.attack(aaa, ccc)
    time.sleep(2)
print ("Fight ended!")

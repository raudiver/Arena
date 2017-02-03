#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time


class Styles(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def report(message):
    print(Styles.OKBLUE, 'SYSTEM: {}'.format(message), Styles.ENDC)


class Dice(object):
    side = range(1, 6)

    def throw(self):
        x = random.choice(self.side)
        print('\tDice result:', x)
        return x


def attack(unit, attacked, dice_value):
    if unit.alive and attacked.alive:
        actual_acc = unit.acc + dice_value
        time.sleep(2)
        if actual_acc > attacked.dodge:
            attacked.hit(unit.damage)

            report('{0} hit {1} on: {2}. {1} has {3} hp left.'.format(unit.name,
                                                                      attacked.name,
                                                                      unit.damage,
                                                                      attacked.health))
        else:
            time.sleep(2)
            print(Styles.BOLD, '{} missed on {}!'.format(unit.name,
                                                         attacked.name), Styles.ENDC)


class ArenaOneByOne(object):
    def __init__(self, hero, enemy, dice=Dice()):
        self._hero = hero
        self._enemy = enemy
        self._dice = dice

        # TODO: Replace all pint on output function
        print(Styles.OKGREEN, 'HERO: What inside this cave?', Styles.ENDC)
        print(Styles.WARNING, 'ENEMY: I will crash you!', Styles.ENDC)

    def move(self):
        report('Player is trying to hit monster')

        attack(self._hero, self._enemy, self._dice.throw())

        if not self._enemy.alive:
            print(Styles.FAIL, 'ENEMY: Is over...', Styles.ENDC)
            return

        time.sleep(2)
        attack(self._enemy, self._hero, self._dice.throw())

        if not self._enemy.alive:
            print(Styles.FAIL, 'WASTED!', Styles.ENDC)

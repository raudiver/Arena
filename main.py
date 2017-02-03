#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from modules.unit import Unit
from arenas.one_by_one import ArenaOneByOne
from arenas.log import Log

SPEECH_HERO = ['What inside this cave?', 'One more monster?', 'Maybe here is empty?', '...']
SPEECH_ENEMY = ['I will crash you!', 'I will smash your head you!', 'Arrr.....', 'Are you tasty?']


def main():
    hero = Unit(name='Hero',
                health=10,
                damage=2,
                dodge=4,
                acc=2,
                speech=SPEECH_HERO)

    enemy = Unit(name='Orc',
                 health=6,
                 damage=3,
                 dodge=3,
                 acc=3,
                 speech=SPEECH_ENEMY)
    log = Log()
    arena = ArenaOneByOne(hero, enemy, log)

    while hero.alive and enemy.alive:
        arena.move()
        time.sleep(2)

    log.end_fight()


if __name__ == '__main__':
    main()

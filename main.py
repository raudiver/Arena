#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from modules.unit import Unit
from arenas.one_by_one import ArenaOneByOne
from arenas.log import Log

SPEECH_HERO = ['What inside this cave?', 'One more monster?', 'Maybe here is empty?', '...']
SPEECH_ENEMY = ['I will crash you!', 'I will smash your head!', 'Arrr.....', 'Are you tasty?']


def main():
    hero = Unit(name='Hero',
                health=10,
                damage=2,
                dodge=4,
                acc=2,
                speech=SPEECH_HERO)

    enemys = [Unit(name='Orc',
                   health=6,
                   damage=3,
                   dodge=3,
                   acc=3,
                   speech=SPEECH_ENEMY),
              Unit(name='Mayor Orc',
                   health=40,
                   damage=20,
                   dodge=16,
                   acc=9,
                   speech=SPEECH_ENEMY),
              Unit(name='General Orc',
                   health=80,
                   damage=60,
                   dodge=20,
                   acc=18,
                   speech=SPEECH_ENEMY)]

    log = Log()

    # Tower mode
    for index, enemy in enumerate(enemys):
        log.stair(index)
        arena = ArenaOneByOne(hero, enemy, log)

        while hero.alive and enemy.alive:
            arena.move()
            time.sleep(2)

        if not hero.alive:
            break

    log.end_fight()


if __name__ == '__main__':
    main()

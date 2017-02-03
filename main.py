#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from modules.unit import Unit
from arenas.one_by_one import ArenaOneByOne


def main():
    hero = Unit(name='Hero',
                health=10,
                damage=2,
                dodge=4,
                acc=2)

    enemy = Unit(name='Orc',
                 health=6,
                 damage=3,
                 dodge=3,
                 acc=3)

    arena = ArenaOneByOne(hero, enemy)

    while hero.alive and enemy.alive:
        arena.move()
        time.sleep(2)

    print('Fight ended!')


if __name__ == '__main__':
    main()

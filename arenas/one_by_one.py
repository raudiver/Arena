#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time

SUCCESS_HIT_EXPERIENCE_VALUE = 12
MISS_HIT_EXPERIENCE_VALUE = 7


class Dice(object):
    side = range(1, 6)

    def throw(self):
        x = random.choice(self.side)
        return x


def default_attack(unit, attacked, dice_value, log):
    if unit.alive and attacked.alive:
        actual_acc = unit.acc + dice_value

        time.sleep(2)
        if actual_acc > attacked.dodge:
            attacked.hit(unit.damage)

            unit.add_experience(SUCCESS_HIT_EXPERIENCE_VALUE)
            log.hit(unit, attacked)
        else:
            time.sleep(2)

            unit.add_experience(MISS_HIT_EXPERIENCE_VALUE)
            log.miss(unit, attacked)


class ArenaOneByOne(object):
    def __init__(self, hero, enemy, log, attack=default_attack, dice=Dice()):
        self._hero = hero
        self._enemy = enemy
        self._dice = dice
        self._log = log
        self._attack = attack

        self._round = 1

        self._log.player(self._hero)
        self._log.enemy(self._enemy)

    def _unit_move(self, unit, attacked):
        dice_value = self._dice.throw()
        self._log.dice_status(unit, dice_value)
        self._attack(unit, attacked, dice_value, self._log)

    def move(self):
        if not self._hero.alive or not self._enemy.alive:
            return

        self._log.round_start(self._round)

        self._unit_move(self._hero, self._enemy)

        if not self._enemy.alive:
            self._log.enemy_down(self._enemy)
            return

        time.sleep(2)
        self._unit_move(self._enemy, self._hero)

        if not self._hero.alive:
            self._log.player_down(self._hero)

        self._round += 1

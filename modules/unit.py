#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

DAMAGE_FACTOR = 0.12
DODGE_FACTOR = 0.02


class Unit(object):
    # TODO: Add equipment
    def __init__(self, name, health, damage, dodge, acc, speech):
        self._name = name
        self._health = health
        self._damage = damage
        self._dodge = dodge
        self._acc = acc
        self._speech = speech
        self._experience = 1

    @property
    def name(self):
        return self._name

    @property
    def alive(self):
        return self._health > 0

    @property
    def health(self):
        return self._health

    @property
    def damage(self):
        return self._damage * (self._experience * DAMAGE_FACTOR)

    @property
    def dodge(self):
        return self._dodge * (self._experience * DODGE_FACTOR)

    @property
    def acc(self):
        return self._acc

    @property
    def status(self):
        return '{}: health {}, damage {}, dodge {}, acc {}'.format(self.name,
                                                                   self.health,
                                                                   self._damage,
                                                                   self._dodge,
                                                                   self._acc)

    def say(self):
        return self._speech[random.randint(0, len(self._speech) - 1)]

    def hit(self, damage):
        self._health -= damage

    def add_experience(self, value):
        self._experience += value

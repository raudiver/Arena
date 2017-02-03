#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Styles(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Log(object):
    def __init__(self):
        pass

    # TODO: Replace pint on output function
    def print(self, message, decorator=None):
        if decorator:
            print(decorator, message, Styles.ENDC)
            return
        print(message)

    def _arena_status(self, message):
        self.print(message='Arena: {0}'.format(message),
                   decorator=Styles.OKBLUE)

    def hit(self, unit, attacked):
        self._arena_status(message='{0} hit {1} on: {2}. {1} has {3} hp left.'.format(unit.name,
                                                                                      attacked.name,
                                                                                      unit.damage,
                                                                                      attacked.health))

    def miss(self, unit, attacked):
        self.print(message='{} missed on {}!'.format(unit.name,
                                                     attacked.name),
                   decorator=Styles.BOLD)

    def _unit_speech(self, unit, decorator):
        self.print(message='{}: {}'.format(unit.name,
                                           unit.say()),
                   decorator=decorator)

    def player(self, player):
        self._unit_speech(unit=player,
                          decorator=Styles.OKGREEN)

    def enemy(self, enemy):
        self._unit_speech(unit=enemy,
                          decorator=Styles.WARNING)

    def _unit_down(self, unit, message):
        self.print(message='{}: {}'.format(unit.name,
                                           message),

                   decorator=Styles.FAIL)

    def player_down(self, player):
        self._unit_down(unit=player,
                        message='WASTED!')

    def enemy_down(self, enemy):
        self._unit_down(unit=enemy,
                        message='Is over...')

    def round_start(self, round):
        self.print('Round: {}'.format(round))

    def end_fight(self):
        self.print('Fight ended!')

    def dice_status(self, value):
        self.print('\tDice result: {}'.format(value))

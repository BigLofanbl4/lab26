#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class Human:
    def __init__(self, id, team):
        self.id = id
        self.team = team


class Soldier(Human):
    def __init__(self, id, team):
        super().__init__(id, team)

    def follow_hero(self, hero):
        print(f"Soldier {self.id} follows {hero.id} team {self.team}")


class Hero(Human):
    def __init__(self, id, team):
        super().__init__(id, team)
        self.level = 1

    def increase_level(self):
        self.level += 1


if __name__ == "__main__":
    red_hero = Hero("red_hero", "Blue")
    blue_hero = Hero("blue_hero", "Red")

    blue_soldiers = []
    red_soldiers = []

    for i in range(50):
        team = random.choice(["Blue", "Red"])
        if team == "Blue":
            blue_soldiers.append(Soldier(i, "Blue"))
        else:
            red_soldiers.append(Soldier(i, "Red"))

    print(f"Team blue has {len(blue_soldiers)} soldiers")
    print(f"Team red has {len(red_soldiers)} soldiers")

    if len(blue_soldiers) > len(red_soldiers):
        blue_hero.increase_level()
        blue_soldiers[0].follow_hero(blue_hero)
        print(blue_hero.id, blue_soldiers[0].id)
    else:
        red_hero.increase_level()
        red_soldiers[0].follow_hero(red_hero)
        print(red_hero.id, red_soldiers[0].id)

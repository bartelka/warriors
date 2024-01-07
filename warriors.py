class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
        self.is_alive = True if health > 0 else False


class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        super().__init__(health, attack)


def fight(w1, w2):
    while w1.is_alive and w2.is_alive:
        w2.health -= w1.attack
        w2.is_alive = True if w2.health > 0 else False
        if w2.is_alive:
            w1.health -= w2.attack
            w1.is_alive = True if w1.health > 0 else False
        else:
            break
    return w1.is_alive


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit, count):
        for _ in range(count):
            self.units.append(unit())



class Battle:
    def fight(self, army_1, army_2):
        while len(army_1.units) > 0 and len(army_2.units) > 0:
            unit_1 = army_1.units[0]
            unit_2 = army_2.units[0]

            while unit_1.is_alive and unit_2.is_alive:
                unit_2.health -= unit_1.attack
                unit_2.is_alive = True if unit_2.health > 0 else False
                if unit_2.is_alive:
                    unit_1.health -= unit_2.attack
                    unit_1.is_alive = True if unit_1.health > 0 else False
                else:
                    break

            if unit_1.is_alive:
                army_2.units.pop(0)
            else:
                army_1.units.pop(0)

        return True if len(army_1.units) > 0 and len(army_2.units) == 0 else False



chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

print(fight(chuck, bruce))
print(fight(dave, carl))

my_army = Army()
my_army.add_units(Knight, 3)

enemy_army = Army()
enemy_army.add_units(Warrior, 3)

army_3 = Army()
army_3.add_units(Warrior, 20)
army_3.add_units(Knight, 5)

army_4 = Army()
army_4.add_units(Warrior, 30)

battle = Battle()
print(battle.fight(my_army, enemy_army))
print(battle.fight(army_3, army_4))


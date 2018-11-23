import random

# Hero Class
# YES
class Hero:
    def __init__(self, name, starting_health=100):
         self.name = name
         self.abilities = list()
         self.starting_health = starting_health
         self.current_health = starting_health
         # self.armors = ()
         # self.deaths = 0
         # self.kills  = 0

    # YES
    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)
    #YES
    def add_weapon(self, weapon):
        '''Add weapon to abilities list'''
        self.abilities.append(weapon)
    #YES
    def add_armor(self, armor):
        '''Add armor object to armor list'''
        self.armors.append(armor)
    # YES
    def attack(self):
        '''Calculate damage from abilities list
        Calls Ability.attack()on every ability in self.abilities and returns total'''
        total = 0
        for ability in range(len(self.abilities)):
            total += self.abilities[ability].attack()
        return total
    # MAYBE
    def take_damage(self, damage):
        '''Update self.current_health with the damage passed in'''
        self.current_health -= damage - self.defend()
    # MAYBE
    def is_alive(self):
         '''Boolean. Return true if hero is alive, false if not'''
         if self.current_health > 0:
            return True
         else:
            print('{} is forever gone'.format(self.name))
            return False
    # MAYBE
    def fight(self, opponent):
         '''Runs a loop to attack the opponent until someone dies'''
         while self.is_alive() and opponent.is_alive():
             self.take_damage(opponent.attack())
             opponent.take_damage(self.attack())
         if not self.is_alive():
             opponent.add_kill(1)
             print("{} is forever gone".format(self.name))
         elif not opponent.is_alive():
             self.add_kill(1)

# YES
class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength
    # PROBABLY
    def attack(self):
        '''Return random attack value between 0 and max_damage'''
        return random.randint(0, int(self.attack_strength))

# MAYBE
class Weapon(Ability):
    def attack(self):
        """Return a random value between half-full weapon attack power"""
        return random.randint((self.attack_strength//2), self.attack_strength)

# YES so far
class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()
    # YES
    def add_hero(self, hero):
        '''Add Hero object to heroes list'''
          self.heroes.append(hero)
    # MAYBE/IFFY
    def remove_hero(self, name):
        '''Remove hero from heroes list. If Hero isn't found return 0'''
        if not (len(self.heroes) > 0):
            return 0
        else:
            for hero_obj in self.heroes:
                if hero_obj.name == name:
                    self.heroes.remove(hero_obj)
                else:
                    return 0
    # MAYBE
     def view_all_heroes(self):
        '''Print all heroes to the console.'''
          for hero in self.heroes:
              print(hero.name)


class Armor:
    def __init__(self, name, max_block):
        '''Instantiate name and defense strength'''
        self.name = name
        self.max_block = max_block





#
#     game_is_running = True
#     arena = Arena()
#     arena.build_team_one()
#     arena.build_team_two()
#
#     while game_is_running:
#         arena.team_battle()
#         arena.show_stats()
#
#         play_again = raw_input("Would you want to play again? Y or N: ")
#
#         if play_again.lower() == "n":
#             game_is_running = False
#         else:
#             arena.team_one.revive_heroes()
#             arena.team_two.revive_heroes()


if __name__ == "__main__":
    # TESTS
    # YES
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 20)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 30)
    hero.add_ability(new_ability)
    print(hero.attack())
    # NOT YET
    # hero2 = Hero("Jodie Foster")
    # ability2 = Ability("Science", 800)
    # hero2.add_ability(ability2)
    # hero.fight(hero2)

    print (__name__)

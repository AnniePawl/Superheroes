import random

# Hero Class
# YES
class Hero:
    def __init__(self, name, starting_health=100):
         self.name = name
         self.abilities = list()
         self.starting_health = starting_health
         self.current_health = starting_health
         self.armors = list()
         self.deaths = 0
         self.kills  = 0

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
    # MAYBE
    def defend(self):
          total_block = 0
          if self.current_health == 0:
            return 0
          else:
            for armor in self.armors:
                total_block += armor.block()
                return total_block
    # YES
    def attack(self):
        '''Calculate damage from abilities list
        Calls Ability.attack()on every ability in self.abilities and returns total'''
        total = 0
        for ability in self.abilities:
        # for ability in range(len(self.abilities)):
            total += ability.attack()
        return total
    # MAYBE
    def take_damage(self, damage):
        '''Update self.current_health with the damage passed in'''
        self.current_health -= damage - self.defend()
    # YES
    def add_kill(self, num_kills):
        '''track number of kills'''
        self.kills += num_kills

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
        return random.randint((self.attack_strength//2),self.attack_strength)

# YES
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
    # Experimenting
    def attack(self, other_team):
        '''randomly select living hero from each team, fight until a team has no heroes'''
        while len(self.alive_heroes()) > 0 and len(other_team.alive_heroes()) > 0:
            random_hero_1 = random.choice(self.alive_heroes())
            random_hero_2 = random.choice(other_team.alive_heroes())
            random_hero_1.fight(random_hero_2)
    # Maybe
    def revive_heroes(self, health=100):
      '''reset hero health'''
      for hero in self.heroes:
            Hero.current_health = health
            return Hero.current_health

    def stats(self):
        '''prints kill/death ratio for teammates'''
        for hero in self.heroes:
            hero.show_stats()



         # while self.healthCheck() and other_team.healthCheck():
         #    self.heroes[random.randint(0, len(self.heroes)-1)].fight(other_team.heroes[random.randint(0, len(other_team.heroes)-1)])
    # MAYBE
    def view_all_heroes(self):
        '''Print all heroes to the console.'''
        for hero in self.heroes:
            print(hero.name)
            # print("{}".format(hero.name))


# YES
class Armor:
    def __init__(self, name, max_block):
        '''Instantiate name and defense strength'''
        self.name = name
        self.max_block = max_block
    # YES
    def block(self):
        '''return random value between 0-max_block strength'''
        return random.randint(0, int(self.max_block))

# Arena takes care of creating heroes and adding them to their respective teams
# YES
class Arena:
    def __init__(self):

        self.team_one = None
        self.team_two = None

    # Create Hero Method ?
    # Create Ability Method?
    # Create Weapon Method?
    # Create Armor Method?

    #YES
    def build_team_one(self):
        """Build 1st team """
        print('Putting team one together ....')
        name = input("Choose a team name: ")
        self.team_one = Team(name)
        return self.team_one

    #YES
    def build_team_two(self):
        """enables team 2 creation"""
        print('Putting team two together ...')
        name = input("Choose another team name: ")
        self.team_two = Team(name)
        return self.team_two

    def team_battle(self):
        '''fights two teams'''
        while self.team_one.alive_heroes() and self.team_two.alive_heroes():
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
        if self.team_one.alive_heroes():
            print('{} team won the battle!'.format(self.team_one.name))
            self.team_one.update_kills(len(self.team_two.heroes))
            return False
        else:
            print('{} team won the battle!'.format(self.team_two.name))
            self.team_two.update_kills(len(self.team_one.heroes))
            return False

    # YES
    def show_stats(self):
        """Print hero in arena stats(kill/death ratio) """
        print('Printing stats')
        self.team_one.stats()
        self.team_two.stats()

# GAME LOOP
if __name__ == "__main__":
    game_is_running = True

    arena = Arena()
    # Build teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N:")
        # Check player input
        if play_again.lower() == "n":
            game_is_running = false
        else:
            # Revive heroes n play again
            area.team_one.revive_heroes()
            area.team_two.revive_heroes()










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

    print (hero.name)

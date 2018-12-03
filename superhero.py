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
            total += ability.attack()
        return total

    # MAYBE
    def take_damage(self, damage):
        '''Update self.current_health with the damage passed in'''
        # CHANGE - Add min() so that defense does not exceed damage.
        self.current_health -= damage - min(damage, self.defend())

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
            return False

    # MAYBE
    def fight(self, opponent):
        '''Runs a loop to attack the opponent until someone dies'''
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if not self.is_alive():
            self.deaths += 1
            opponent.add_kill(1)
            print()
            print("{} killed {}".format(opponent.name, self.name))
            print()
        if not opponent.is_alive():
            opponent.deaths += 1
            self.add_kill(1)
            print("{} killed {}".format(self.name, opponent.name))


    def show_stats(self):
        if self.deaths == 0:
            kdr = "inf"
        else:
            kdr = self.kills / self.deaths
        print("KDR for %s: %s" % (self.name, kdr))

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
                    return 1
        return 0

    def alive_heroes(self):
        alive_heroes = []
        for hero in self.heroes:
        	if hero.is_alive():
        		alive_heroes.append(hero)
        return alive_heroes

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
            hero.current_health = health

    def stats(self):
        '''prints kill/death ratio for teammates'''
        print()
        print("Showing Stats for Team %s" % self.name)
        for hero in self.heroes:
            hero.show_stats()

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

    def create_ability(self):
        print("CREATING A NEW ABILITY")
        name = input("Ability name: ")
        attack_strength = int(input("Ability attack strength: "))
        print()
        return Ability(name, attack_strength)

    def create_weapon(self):
        print("CREATING A NEW WEAPON")
        name = input("Weapon name: ")
        attack_strength = int(input("Weapon attack strength: "))
        print()
        return Weapon(name, attack_strength)

    def create_armor(self):
        print("CREATING NEW ARMOR")
        name = input("Armor name: ")
        max_block = int(input("Armor max block: "))
        print()
        return Armor(name, max_block)

    def create_hero(self):
        print("CREATING NEW HERO")
        name = input("Hero name: ")
        hero = Hero(name)
        while True:
            create_option = input("What do you want to add? <armor, ability, weapon, none>: ")
            if create_option == "none":
                # No more creating, so break loop.
                break
            elif create_option == "armor":
                hero.add_armor(self.create_armor())
            elif create_option == "ability":
                hero.add_ability(self.create_ability())
            elif create_option == "weapon":
                hero.add_weapon(self.create_weapon())
            else:
                print("Invalid option!")
        return hero
        print()

    #YES
    def build_team_one(self):
        """Build 1st team """
        print('Putting team one together ....')
        name = input("Choose a team name: ")
        self.team_one = Team(name)
        num_heroes = int(input("Num heroes: "))
        for _ in range(num_heroes):
            self.team_one.add_hero(self.create_hero())

    #YES
    def build_team_two(self):
        """Build 2nd team """
        print('Putting team two together ....')
        name = input("Choose a team name: ")
        self.team_two = Team(name)
        num_heroes = int(input("Num heroes: "))
        for _ in range(num_heroes):
            self.team_two.add_hero(self.create_hero())

    def team_battle(self):
        '''fights two teams'''
        self.team_one.attack(self.team_two)
        print()
        if self.team_one.alive_heroes():
            print('{} team won the battle!'.format(self.team_one.name))
        elif self.team_two.alive_heroes():
            print('{} team won the battle!'.format(self.team_two.name))
        else:
            print("BOTH TEAMS DESTROYED EACHOTHER!")

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
        print()
        play_again = input("Play Again? Y or N:")
        # Check player input
        if play_again.lower() == "n":
           game_is_running = False
        else:
           # Revive heroes n play again
           arena.team_one.revive_heroes()
           arena.team_two.revive_heroes()

    # # TESTS
    # hero = Hero("Wonder Woman")
    # print(hero.attack())
    # ability = Ability("Divine Speed", 20)
    # hero.add_ability(ability)
    # print(hero.attack())
    # new_ability = Ability("Super Human Strength", 30)
    # hero.add_ability(new_ability)
    # print(hero.attack())
    # hero2 = Hero("Jodie Foster")
    # ability2 = Ability("Science", 800)
    # hero2.add_ability(ability2)
    # # hero.fight(hero2)
    # hero2.fight(hero)
    # print("Jodie Foster num kills: %s" % hero2.kills)
    # print("Jodie Foster num deaths: %s" % hero2.deaths)
    # print("Wonder Woman num kills: %s" % hero.kills)
    # print("Wonder Woman num deaths: %s" % hero.deaths)
    # print (hero.name)

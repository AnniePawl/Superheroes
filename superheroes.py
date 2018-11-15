# Hero Class
# Initialize values as instance variables
class Hero:
    def __init__(self, name, starting_health=100):
         self.name = name
         self.abilities = list()
         self.starting_health = starting_health
         self.current_health = starting_health

    # Add ability to ability list
    def add_ability(self, ability):
        self.abilities.append(ability)

    # Calculate damange from abilities
    # Call Ability.attack() on every ability in self.ability, then return total
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    # Update self.current_health with damage
    def take_damage(self, damage):
        pass

    # Return true if hero is alive, return false if dead
    def is_alive(self):
        pass

    # Loop to attack opponent until someone dies
    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
# Initialize values as instance variables

class Ability:
    def __init__(self, name, max_damage):
        pass

    # Return random attack value between 0 and max_damage
    def attack(self):
        pass

if __name__ == "__main__":

    game_is_running = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()

        play_again = raw_input("Would you want to play again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

    # If you run this file from the terminal
    # this block is executed.
    pass

    # TESTS
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
     hero.add_ability(new_ability)
    print(hero.attack())

    print (__name__)

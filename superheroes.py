class Hero:
    def __init__(self, name, starting_health=100):
        '''
        Initialize these values as instance variables:
        (Some of these values are passed in above, others will need to be set at a starting value.)
        abilities:List
        name:
        starting_health:
        current_health:
         '''
         pass


    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        pass

    def attack(self):
        '''
        Calculates damage from list of abilities.

        This method should call Ability.attack()
        on every ability in self.abilities and
        return the total.
        '''
        pass

    def take_damage(self, damage):
        '''
        This method should update self.current_health
        with the damage that is passed in.
        '''
        pass

    def is_alive(self):
        '''
        This function will
        return true if the hero is alive
        or false if they are not.
        '''
        pass

    def fight(self, opponent):
        '''
        Runs a loop to attack the opponent until someone dies.
        '''
        pass

class Ability:
    def __init__(self, name, max_damage):
        '''
        Initialize the values passed into this
        method as instance variables.
         '''
        pass

    def attack(self):
        '''
        Return a random attack value
        between 0 and max_damage.
        '''
        pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    pass

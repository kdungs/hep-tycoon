GLOBAL_SKILL = 1

def random_name():
    from random import choice
    """
        Construct a random name for a scientist.
    """
    first_names = ['Hans', 'Peter', 'Klaus', 'Kevin', 'Lennaert']
    last_names = ['Hansen', 'Petersen', 'Klausen', 'Dungs', 'Maguire', 'Bel']
    return '{} {}'.format(choice(first_names), choice(last_names))


class Scientist:
    """
        A scientist in the game.
    """
    def __init__(self, salary):
        self._name = random_name()
        self._salary = salary
        self._skill = GLOBAL_SKILL

    def __str__(self):
        """
            Return a string identifying the scientist.
            At this point it's just the name since skill and salary are the same for all of them.
        """
        return '{}'.format(self._name)

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def skill(self):
        return self._skill

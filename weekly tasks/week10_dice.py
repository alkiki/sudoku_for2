import random


class Dice:
    def __init__(self, slides):
        self.slides = slides

    def roll(self):
        return random.randint(1, self.slides)

    def change_num_of_sides(self, sides):
        self.sides = sides

    def roll_multiple(self, times):
        result = []
        for i in range(0, times):
            self.roll()
            result.append(self.roll())
        return result


dice = Dice(6)
print(dice.roll_multiple(4))


class SetOfDice:
    dice = []

    def __init__(self):
        pass

    def add_dice(self):
        self.dice.append(dice)

    def remove_dice(self):
        self.dice


collection = SetOfDice()
collection.add_dice()

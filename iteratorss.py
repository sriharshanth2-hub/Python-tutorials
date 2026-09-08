import random
class Dice :
    def __init__(self,roll):
        self.roll = roll
        self.count = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.count < self.roll :
            self.count += 1
            return random.randint(1,6)
        else :
            raise StopIteration
        
dice  = Dice(3)
for die in dice :
    print(die)

        
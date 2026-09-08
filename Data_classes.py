from dataclasses import dataclass,field
@dataclass
class food :
    name : str
    taste : int 
    ingridients : str = field(repr = False)
    is_hot : bool = True
    def __post_init__(self) :
        if self.taste < 0 or self.taste > 10 :
            raise ValueError("Taste cannot exceed above 10 or go below 0")
        
food_1 = food("chicken curry",8,"cashew paste")
food_2 = food("fish fry",9,"fish masala")
print(food_1)
print(food_2)
print(food_1 == food_2)




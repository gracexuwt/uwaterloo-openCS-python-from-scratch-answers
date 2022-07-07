class Meal:
    """Meal name, cost, and list of allergens

       Public methods:
       __init__: initializes a new object

       Attributes:
       name: non-empty string; meal name
       cost: int >= 0; cost of meal
       allergens: list of strings; allergens
    """
    
    def __init__(self, name, cost, allergens):
        self.name = name
        self.cost = cost
        self.allergens = allergens
        
    def contains(self, food):
        if(food in self.allergens):
            return True
        return False
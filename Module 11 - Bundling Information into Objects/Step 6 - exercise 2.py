class Egg:
    """Egg low and high range of mass
       and category name.
    
       Attributes:
       low: int > 0, lowest mass in grams
       high: int > 0, highest mass in grams
       name: nonempty string, category
    """
    def __init__(self, low, high, name):
        self.low = low
        self.high = high
        self.name = name

    def __str__(self):
        return name
        
    def is_size(self, num):
        if(self.low <= num <= self.high):
            return True
        return False
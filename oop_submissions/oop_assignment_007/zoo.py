class Deer:
    sound = "Buck Buck"
    breath = "Breathe in air"
    def __init__(self, age_in_months = 1, breed = None, required_food_in_kgs = 0):
        if required_food_in_kgs == 0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        if age_in_months == required_food_in_kgs:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        if age_in_months > required_food_in_kgs:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
    
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    def grow(self):
        if self._required_food_in_kgs:
            self._required_food_in_kgs += 2
        if self._age_in_months:
            self._age_in_months += 1
    @classmethod       
    def make_sound(cls):
        print(cls.sound)
    @classmethod
    def breathe(cls):
        print(cls.breath)

class Lion(Deer):
    sound = "Roar Roar"
    breath = "Breathe in air"
    def grow(self):
        if self._required_food_in_kgs:
            self._required_food_in_kgs += 4
        if self._age_in_months:
            self._age_in_months += 1
            
    
        
class Shark(Deer):
    sound ="Shark Sound"
    breath = "Breathe oxygen from water"
    def grow(self):
        if self._required_food_in_kgs:
            self._required_food_in_kgs += 8
        if self._age_in_months:
            self._age_in_months += 1           

class GoldFish(Deer):
    sound = "Hum Hum"
    breath = "Breathe oxygen from water"
   
    def grow(self):
        if self._required_food_in_kgs:
            self._required_food_in_kgs += 0.2
        if self._age_in_months:
            self._age_in_months += 1
        
class Snake(Deer):
    sound = 'Hiss Hiss'
    breath = "Breathe in air"
    def grow(self):
        if self._required_food_in_kgs:
            self._required_food_in_kgs += 0.5
        if self._age_in_months:
            self._age_in_months += 1
  
    

class Zoo:
    
    def __init__(self,reserved_food_in_kgs = 0):
        self._animal_list = []
        self._reserved_food_in_kgs = reserved_food_in_kgs
      
    @property  
    def animal_list(self):
        return self._animal_list
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    def add_animal(self, value = None):
        return self._animal_list.append(type(value).__name__)
        
    
    def count_animals(self):
        return len(self._animal_list)
        
    def add_food_to_reserve(self, food_in_kgs):
        self._reserved_food_in_kgs += food_in_kgs
        return self._reserved_food_in_kgs
    
    def feed(self, obj = None):
        if self._reserved_food_in_kgs != 0:
            self._reserved_food_in_kgs -= obj._required_food_in_kgs
            obj.grow()
    
'''    
nehru_zoological_park = Zoo()

lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)

deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
nehru_zoological_park.add_animal(deer)
nehru_zoological_park.count_animals()

lion.hunt(nehru_zoological_park)
print(nehru_zoological_park.count_animals())
lion.hunt(nehru_zoological_park) # Prints
class Animal:
    def hunt(self, obje= None):
        if type(self).__name__ in("Lion", "Snake"):
            if obje.animal_list.count("Deer") > 0:
                obje.animal_list.remove("Deer")
            else:
                print("No deer to hunt")
        elif type(self).__name__ == "Shark":
            if obje.animal_list.count("GoldFish") > 0:
                obje.animal_list.remove("GoldFish")
            else:
                print("No GoldFish to hunt")

'''        
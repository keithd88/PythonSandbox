### Creating a Class
class Home:
    def __init__(self, rooms=3, stories=1):
        # set instance variables
        self.rooms = rooms
        self.stories = stories

my_home = Home()


### Attributes
class Bird:
    is_hungry = True

parakeet = Bird()
parrot = Bird()

print("Birds are hungry!")
print("Feeding birds...")

parakeet.is_hungry = False
parrot.is_hungry = False

print("Birds fed!")


### Methods
class Bird:
    is_hungry = True

    def feed_bird(self, food):
        if(self.is_hungry):
            self.is_hungry = False
            print(f"Feeding with {food}. Bird fed!")
        else:
            print("Bird isn't hungry right now.")

sparrow = Bird()

sparrow.feed_bird('seeds')
sparrow.feed_bird('oats')


# Static Methods
class Home:
    name = "Code Ninja"
    rooms = 4
    stories = 2

    @staticmethod
    def is_on_market(home):
        if(home.name == ""):
            return True
        else:
            return False
        
    @classmethod
    def paint_wall(self, color):
        return f"Painting wall {color}."
    
home = Home()

print(Home.is_on_market(home))



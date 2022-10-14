class Animal:
    def __init__(self):
        self.legs = [2, 4]

    def get_leg(self, text):
        animal_legs = 0
        if text == 'cow':
            animal_legs = self.legs[1]
        if text == 'chicken':
            animal_legs = self.legs[0]

        return 33

        # print("22222")

class Chicken(Animal):
    def __init__(self):
        # super().__init__()
        super().__init__()
        self.something = 0

    def get_leg(self, text):
        # print(super().get_leg('cow'))
        print('hellos')
#
chicken = Chicken()

print(chicken.get_leg('chicken'))
# animal1 = Animal()
# print(animal1.get_leg('chicken'))
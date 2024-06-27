class Bike:

    wheels_count = 2# static variable -> for all objects of this class

    def __init__(self, color: str):#str - only suggestion
        self.color = color

    def info(self):
        print(f'This bike\'s color is {self.color} and it has {self.wheels_count} wheels.')


rowery = (Bike('green'), Bike('brown'), Bike('cyan'))

for bike in rowery:
    bike.info()

Bike.wheels_count = 3
print("Something went wrong and bikes have now " + str(rowery[0].wheels_count) + " wheels.")
print("Something went wrong and bikes have now " + str(Bike.wheels_count) + " wheels.")

bike4 = Bike(3)
bike4.info()

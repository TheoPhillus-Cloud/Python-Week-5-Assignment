class Transport:
    def move(self):
        pass

# Subclass: Car
class Car(Transport):
    def move(self):
        return "Driving on the road "

# Subclass: Plane
class Plane(Transport):
    def move(self):
        return "Flying in the sky "

# Subclass: Boat
class Boat(Transport):
    def move(self):
        return "Sailing on the water "

# Usage
Transport = [Car(), Plane(), Boat()]

for Transport in Transport:
    print(Transport.move())
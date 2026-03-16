'''
                                vehicle
                                usage : transportation


wheels : 4                                                 wheels : 2
has roof : yes                                          has roof : no
specific usage : vacation with  family   specific : racing
'''

class vehicle: # parent
    def general_usage(self):
        print("General use : Transaportation")

class car(vehicle): # child
    def __init__(self):
        print("i'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage() # self is obj of car class it is derived from vehicle
        print("commute to work , vacation with family")


class motor_cycle(vehicle):
    def __init__(self):
        print("i'm Bicycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()  # self is obj of car class it is derived from vehicle
        print("Road Trip,Racing")

c = car() # create a obj
c.specific_usage() # calling methods

m = motor_cycle()
m.specific_usage()

'''
Benefits

1) code Reuse  2) Extensibility 3) Readability

is instance and is subclass methods
Built in func
'''

print(isinstance(c,car))
print(isinstance(c,motor_cycle))
print("***************************")
print(isinstance(car,vehicle))
print(issubclass(car,vehicle))
print(issubclass(car,motor_cycle))
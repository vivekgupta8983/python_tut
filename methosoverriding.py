"""
Inheritance is a way of creating new class for using details of existing class without modifying it.
The newly formed class is a derived class (or child class).
Similarly, the existing class is a base class (or parent class).
"""
class Car(object):

    def __init__(self):
        print("You just create the car instance")

    def drive(self):
        print("Car started")

    def stop(self):
        print("Car Stopped")

class BMW(Car):
    def __init__(self):
        Car.__init__(self)
        print("You just created the BMW instance")

    def drive(self):
        print("You are driving a BMW , Enjoy......")

    def headup_display(self):
        print("This is a unique feature")

c = Car()
c.drive()
c.stop()

b = BMW()
b.drive()
b.headup_display()
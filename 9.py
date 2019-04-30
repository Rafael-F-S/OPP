class Car:
    def __init__(self, make, model, owner):
        self.make=make
        self.model=model
        self.owner=owner

    def drive(self):
        print("The car drives away into the sunset...")


test_car = Car("Ford", "Focus", "Emily")
test_car.drive()
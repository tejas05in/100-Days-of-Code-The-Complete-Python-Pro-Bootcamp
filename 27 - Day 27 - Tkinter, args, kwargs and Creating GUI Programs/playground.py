def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result
def calculate(n , **kwargs):
    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")
if __name__ == '__main__':
    # print(add(2,3,4,56,))
    # calculate(2, add=3, multiply=5)
    my_car = Car(make="Nissan",model="Skyline")
    print(my_car.make)
    print(my_car.model)
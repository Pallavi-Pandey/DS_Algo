#  Inheritance

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    def drive(self):
        print("Driving")

class ElectricCar(Car):
    def __init__(self, color, model, battery):
        super().__init__(color, model)
        self.battery = battery
    def drive(self):
        print("Driving with electric power")

electric_car = ElectricCar("red", "2020", "1000")
electric_car.drive()



# Types of Inheritance:
# 1. Single Inheritance
# Code:

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Animal speaking")

class Dog(Animal):
    def speak(self):
        print("Dog barking")

    def eat(self):
        print("Dog eating")

dog = Dog("Buddy")
dog.speak()
dog.eat()


# 2. Multiple Inheritance
# Code:

class A:
    def method_A(self):
        print("Method A")

class B:
    def method_B(self):
        print("Method B")

class C(A, B):
    def method_C(self):
        print("Method C")

obj = C()
obj.method_A()
obj.method_B()
obj.method_C()


# 3. Multilevel Inheritance
# Code:

class A:
    def method_A(self):
        print("Method A")

class B(A):
    def method_B(self):
        print("Method B")

obj = B()
obj.method_A()
obj.method_B()


# 4. Hierarchical Inheritance
# Code:

class A:
    def method_A(self):
        print("Method A")

class B(A):
    def method_B(self):
        print("Method B")

class C(A):
    def method_C(self):
        print("Method C")

obj = C()
obj.method_A()
obj.method_C()

# 5. Hybrid Inheritance
# Code:

class A:
    def method_A(self):
        print("Method A")

class B(A):
    def method_B(self):
        print("Method B")

class C(B):
    def method_C(self):
        print("Method C")

obj = C()
obj.method_A()
obj.method_B()
obj.method_C()

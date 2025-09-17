# Object Oriented Programming
 - Object Oriented Programming is a programming paradigm based on the concept of "objects", which can contain data in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods).
 - Types of OOP:
   - Class
   - Object
   - Inheritance
   - Abstraction 
   - Encapsulation
   - Polymorphism
# Class:
  - Blueprint for creating objects
  - Has attributes and methods
  - Ex: Click Here - [Class](/OOPS/Class.py)
  - Car class
    - class Car:
      - def __init__(self, color, model):
        - self.color = color
        - self.model = model
    
      - def drive(self):
        - print("Driving")

# Object:
  - Instance of a class
  - Created from a class
  - Ex: Click Here - [Object](/OOPS/Class.py) 
    - my_car = Car("red", "2020")
  
# Inheritance:
  - Inheritance allows a class to inherit attributes and methods from another class.
  - Ex: Click Here - [Inheritance](/OOPS/Inheritance.py) 
    - class ElectricCar(Car):
      - pass

  - This allows code reusability.
  - Types of Inheritance:
    - Single Inheritance
    - Multiple Inheritance  
    - Multilevel Inheritance
    - Hierarchical Inheritance
    - Hybrid Inheritance

  - Single Inheritance: [Single Inheritance](/OOPS/Inheritance.py)
    - One class inherits from another class.
    - Ex: 
      - class ElectricCar(Car):
        - pass

  - Multiple Inheritance: [Multiple Inheritance](/OOPS/Inheritance.py)
    - One class inherits from multiple classes.
    - Ex: 
      - class ElectricCar(Car, Battery):
        - pass

  - Multilevel Inheritance: [Multilevel Inheritance](/OOPS/Inheritance.py)
    - One class inherits from another class which in turn inherits from another class.
    - Ex: 
      - class ElectricCar(Car):
        - pass
      - class HybridCar(ElectricCar):
        - pass

  - Hierarchical Inheritance: [Hierarchical Inheritance](/OOPS/Inheritance.py)
    - One class inherits from multiple classes.
    - Ex: 
      - class ElectricCar(Car):
        - pass
      - class HybridCar(Car):
        - pass

  - Hybrid Inheritance: [Hybrid Inheritance](/OOPS/Inheritance.py)
    - Combination of multiple types of inheritance.
    - Ex: 
      - class ElectricCar(Car, Battery):
        - pass
      - class HybridCar(Car):
        - pass

# Abstraction:
  - Hiding the complex implementation details and showing only the necessary features to the user.
  - Ex: Click Here = [Absraction](/OOPS/Absraction.py)
  - class Car:
    - def __init__(self, color, model):
      - self.color = color
      - self.model = model
    - def drive(self):
      - print("Driving")
  - class ElectricCar(Car):
    - def __init__(self, color, model, battery):
      - super().__init__(color, model)
      - self.battery = battery
    - def drive(self):
      - print("Driving with electric power")
  - class HybridCar(Car):
    - def __init__(self, color, model, battery):
      - super().__init__(color, model)
      - self.battery = battery
    - def drive(self):
      - print("Driving with hybrid power")

# Encapsulation:
  - Hiding the internal implementation details of a class from the user.
  - Ex: Click Here - [Encapsulation](/OOPS/Encapsulation.py) 
    - Banking System
    - User should not know how the money is being transferred.
    - User should only know how to transfer money.
    - This is achieved by making the transfer method private.
    - Ex:
      - class Bank:
        - def __init__(self, balance):
          - self.__balance = balance
        - def transfer(self, amount):
          - self.__balance -= amount
        - def get_balance(self):
        - return self.__balance

    - my_bank = Bank(1000)
    - my_bank.transfer(100)
    - print(my_bank.get_balance())

# Polymorphism:
  - Polymorphism means "many forms".
  - It allows methods to have the same name but different implementations.
  - Ex: Click Here - [Polymorphism](/OOPS/Polymorphism.py)
  - class Dog:
    - def speak(self):
      - return "Woof!"
  - class Cat:
    - def speak(self):
      - return "Meow!"

  - def animal_speak(animal):
    - print(animal.speak())

  - dog = Dog()
  - cat = Cat()
  - animal_speak(dog)
  - animal_speak(cat)

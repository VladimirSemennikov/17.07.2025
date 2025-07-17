"""
17.07.2025      Фабричный метод
"""

# def main():
#     print("Клиентский код")
#
# if __name__ == "__main__":
#     main()


# from abc import ABC, abstractmethod
#
# """Базовый класс автомобиля"""
# class Car(ABC):
#     @abstractmethod
#     def drive(self):
#         pass
# """Конкретные классы автомобилей"""
# class Sedan(Car):
#     def drive(self):
#         return "Создание седана"
# class SUV(Car):
#     def drive(self):
#         return "Создание внедорожника"
# class Truck(Car):
#     def drive(self):
#         return  "Создание грузовиков"
#
#
# class CarFactory(ABC):
#     @abstractmethod
#     def create_car(self)-> Car:
#         pass
#
# """конкретные фабрики для каждого типа автомобиля"""
# class SedanFactory(CarFactory):
#     def create_car(self) -> Car:
#         return Sedan()
# class SUVFactory(CarFactory):
#     def create_car(self) -> Car:
#         return SUV()
# class TruckFactory(CarFactory):
#     def create_car(self) -> Car:
#         return Truck()
#
# """Клиентский код"""
# def client_code(factory:CarFactory):
#     car = factory.create_car()
#     print(car.drive())
#
# if __name__ == "__main__":
#     sedan_factory = SedanFactory()
#     client_code(sedan_factory)
#
#     suv_factory = SUVFactory()
#     client_code(suv_factory)
#
#     truck_factory = TruckFactory()
#     client_code(truck_factory)





# from abc import ABC, abstractmethod
#
# """базовый класс животного"""
# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
# """Конкретные классы животных"""
# class Dog(Animal):
#     def speak(self):
#         return "Гав Гав!"
# class Cat(Animal):
#     def speak(self):
#         return "Мяу Мяу!"
# class AnimalFactory(ABC):
#     @abstractmethod
#     def create_animal(self) -> Animal:
#         pass
#
# """Создание конкретных фабрик для каждого животного"""
# class CatFactory(AnimalFactory):
#     def create_animal(self) -> Animal:
#         return Cat()
# class DogFactory(AnimalFactory):
#     def create_animal(self) -> Animal:
#         return Dog()
#
# """Клиентский код"""
# def client_code(factory:AnimalFactory):
#     animal = factory.create_animal()
#     print(animal.speak())
# if __name__ == "__main__":
#     cat_factory = CatFactory()
#     client_code(cat_factory)
#
#     dog_factory = DogFactory()
#     client_code(dog_factory)



from abc import ABC, abstractmethod

class Moped(ABC):
    @abstractmethod
    def vzik(self):
        pass
class Bmw(Moped):
    def vzik(self):
        return "Летим на мопеде бмв"
class Java(Moped):
    def vzik(self):
        return "Летим на мопеде ява"
class Iz(Moped):
    def vzik(self):
        return "Летим на мопеде иж"

class Zavod(ABC):
    @abstractmethod
    def create_moped(self) -> Moped:
        pass
class BmvZavod(Zavod):
    def create_moped(self) -> Moped:
        return Bmw()
class JavaZavod(Zavod):
    def create_moped(self) -> Moped:
        return Java()
class IzZavod(Zavod):
    def create_moped(self) -> Moped:
        return Iz()
def client_code(factory:BmvZavod):
    moped = factory.create_moped()
    print(moped.vzik())

if __name__ == "__main__":
    bmv_factory = BmvZavod()
    client_code(bmv_factory)

    java_factory = JavaZavod()
    client_code(java_factory)

    iz_factory = IzZavod()
    client_code(iz_factory)
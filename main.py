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



# from abc import ABC, abstractmethod
#
# class Moped(ABC):
#     @abstractmethod
#     def vzik(self):
#         pass
# class Bmw(Moped):
#     def vzik(self):
#         return "Создали мопед БМВ"
# class Java(Moped):
#     def vzik(self):
#         return "Создали мопед Ява"
# class Iz(Moped):
#     def vzik(self):
#         return "Создали мопед ИЖ"
#
# class Zavod(ABC):
#     @abstractmethod
#     def create_moped(self) -> Moped:
#         pass
# class BmvZavod(Zavod):
#     def create_moped(self) -> Moped:
#         return Bmw()
# class JavaZavod(Zavod):
#     def create_moped(self) -> Moped:
#         return Java()
# class IzZavod(Zavod):
#     def create_moped(self) -> Moped:
#         return Iz()
# def client_code(factory:BmvZavod):
#     moped = factory.create_moped()
#     print(moped.vzik())
#
# if __name__ == "__main__":
#     bmv_factory = BmvZavod()
#     client_code(bmv_factory)
#
#     java_factory = JavaZavod()
#     client_code(java_factory)
#
#     iz_factory = IzZavod()
#     client_code(iz_factory)




"""Паттерн НАБЛЮДАТЕЛЬ"""

"""Метеостанция"""
# from abc import ABC, abstractmethod
#
# class Observer(ABC):
#     @abstractmethod
#     def update(self, temperature: float):
#         pass
# """Конкретные наблюдатели"""
# class TemperatureDisplay(Observer):
#     def update(self, temperature: float):
#         print(f"Температура на экране: Текущая температура {temperature} ℃")
# class WeatherApp(Observer):
#     def update(self, temperature: float):
#         print(f"Приложение погоды: Текущая температура {temperature} ℃")
#
# """Субъект (издатель)"""
# class WeatherStation:
#     def __init__(self):
#         self._observers = []
#         self._temperature = 0.0
#     def add_observer(self, observer: Observer):
#         self._observers.append(observer)
#     def remove_observer(self, observer: Observer):
#         self._observers.remove(observer)
#
#     def notify_observers(self):
#         for observer in self._observers:
#             observer.update(self._temperature)
#     def set_temperature(self, temperature: float):
#         self._temperature = temperature
#         self.notify_observers()
# """Клиентский код"""
# if __name__ == "__main__":
#     weather_station = WeatherStation()
#
#     #создаем наблюдатели
#     display = TemperatureDisplay()
#     app = WeatherApp()
#
#     #подписываемся на обновления
#     weather_station.add_observer(display)
#     weather_station.add_observer(app)
#     weather_station.remove_observer(display)
#
#
#     #изменяем температуру и уведомлением наблюдателей
#     weather_station.set_temperature(25.0)
#     weather_station.set_temperature(30.0)

"""Пример: Новостной портал

В этом примере у нас будет класс NewsAgency (новостное агентство), которое будет 
уведомлять подписчиков о новых статьях. Подписчики могут быть как обычными пользователями, 
так и другими системами, которые хотят получать обновления."""

from abc import ABC, abstractmethod

# Интерфейс наблюдателя
class Subscriber(ABC):
    @abstractmethod
    def update(self, article: str):
        pass

# Конкретный наблюдатель
class User(Subscriber):
    def __init__(self, name: str):
        self.name = name

    def update(self, article: str):
        print(f"{self.name} получена новая статья: '{article}'")

class NewsApp(Subscriber):
    def update(self, article: str):
        print(f"Новое приложение новостей: Опубликована новая статья: '{article}'\n")

# Субъект (издатель)
class NewsAgency:
    def __init__(self):
        self._subscribers = []
        self._articles = []

    def add_subscriber(self, subscriber: Subscriber):
        self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: Subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self, article: str):
        for subscriber in self._subscribers:
            subscriber.update(article)

    def publish_article(self, article: str):
        self._articles.append(article)
        self.notify_subscribers(article)

# Клиентский код
if __name__ == "__main__":
    news_agency = NewsAgency()

    # Создаем подписчиков
    user1 = User("Alice")
    user2 = User("Bob")
    user3 = User("Petr")
    news_app = NewsApp()

    # Подписываемся на обновления
    news_agency.add_subscriber(user1)
    news_agency.add_subscriber(user2)
    news_agency.add_subscriber(user3)
    news_agency.add_subscriber(news_app)

    # Публикуем новые статьи
    news_agency.publish_article("Breaking News: New Python Version Released!")
    news_agency.publish_article("Tech Update: AI is Transforming Industries")
    news_agency.publish_article("3 новая статья")

    news_agency.remove_subscriber(user2)
    news_agency.publish_article("4 статью получают все кроме 2 узера, потмоу что он отписался!")



class Person:
    def __init__(self, name, age, salary, gender):
        self.name = name  # Имя
        self.age = age  # Возраст
        self.salary = salary  # Зарплата
        self.tax_paid = False  # Налог не уплачен
        self.gender = gender  # Пол
        self.address = None  # Адрес
        self.marital_status = None  # Семейное положение

    def pay_taxes(self, city):
        if not self.tax_paid:
            city.collect_taxes(self.salary)
            self.tax_paid = True
            print(f"{self.name} заплатил налоги в городе {city.name}.")

    def move_to_city(self, new_city):
        if hasattr(self, 'current_city'):
            self.current_city.remove_resident(self)
        self.current_city = new_city
        new_city.add_resident(self)
        print(f"{self.name} переехал в {new_city.name}.")

class City:
    def __init__(self, name, population=0, budget=0):
        self.name = name  # Название города
        self.population = population  # Население
        self.budget = budget  # Бюджет города
        self.residents = []  # Список жителей

    def request_funding(self, amount, county):
        # Запрос финансирования у графства
        county.approve_funding(self, amount)

    def receive_funding(self, amount):
        # Получение финансирования
        self.budget += amount
        print(f"{self.name} получено финансирование в размере {amount}.")

    def collect_taxes(self, amount):
        # Сбор налогов
        self.budget += amount * 0.1  
        print(f"Город {self.name} собрал налоги в размере {amount * 0.1}.")

    def add_resident(self, person):
        # Добавление жителя в город
        self.residents.append(person)
        self.population += 1

    def remove_resident(self, person):
        # Удаление жителя из города
        self.residents.remove(person)
        self.population -= 1

    def info(self):
        return f"Город {self.name}, Население: {self.population}, Бюджет: {self.budget}"

class County:
    def __init__(self, name, budget=0):
        self.name = name  # Название графства
        self.budget = budget  # Бюджет графства
        self.cities = []  # Список городов в графстве

    def add_city(self, city):
        # Добавление города в графство
        self.cities.append(city)

    def approve_funding(self, city, amount):
        # Одобрение финансирования для города
        if self.budget >= amount:
            self.budget -= amount
            city.receive_funding(amount)
            print(f"Графство {self.name} одобрило финансирование в размере {amount} для города {city.name}.")
        else:
            print(f"Графство {self.name} не имеет достаточно средств для одобрения для города {city.name}.")

    def collect_taxes(self):
        # Сбор налогов для графства
        for city in self.cities:
            self.budget += city.budget * 0.05  # Сбор 5% от бюджета города
        print(f"Графство {self.name} собрало налоги. Бюджет графства: {self.budget}.")

    def info(self):
        # Информация о графстве
        return f"Графство {self.name}, Бюджет: {self.budget}, Города: {[city.name for city in self.cities]}"

class Country:
    def __init__(self, name, budget=0, capital=None, currency=None, language=None, area=0, population=0, government_type=None):
        self.name = name  # Название страны
        self.budget = budget  # Бюджет страны
        self.cities = []  # Города в стране
        self.counties = []  
        self.capital = capital  
        self.currency = currency  
        self.language = language  
        self.area = area  
        self.population = population  
        self.government_type = government_type  

    def add_city(self, city):
        self.cities.append(city)

    def add_county(self, county):
        self.counties.append(county)

    def approve_funding(self, city, amount):
      
        if self.budget >= amount:
            self.budget -= amount
            city.receive_funding(amount)
            print(f"Страна {self.name} одобрила финансирование в размере {amount} для города {city.name}.")
        else:
            print(f"Страна {self.name} не имеет достаточно средств для одобрения для города {city.name}.")

    def collect_taxes(self):
        # Сбор налогов для страны
        for county in self.counties:
            self.budget += county.budget * 0.05  
        print(f"Страна {self.name} собрала налоги. Бюджет страны: {self.budget}.")

    def info(self):
        # Информация о стране
        return f"Страна {self.name}, Бюджет: {self.budget}, Столица: {self.capital}, Валюта: {self.currency}, Язык: {self.language}, Площадь: {self.area}, Население: {self.population}, Тип правительства: {self.government_type}"


estonia = Country("Эстония", 1000000, "Таллинн", "Евро", "Эстонский", 45227, 1326535, "Парламентская Республика")
france = Country("Франция", 5000000, "Париж", "Евро", "Французский", 643801, 67413000, "Полупрезидентская Республика")
germany = Country("Германия", 7000000, "Берлин", "Евро", "Немецкий", 357022, 83166711, "Федеративная Республика")

city1 = City("Таллинн", population=430000, budget=500000)
city2 = City("Тарту", population=100000, budget=150000)
city3 = City("Париж", population=2148000, budget=2000000)
city4 = City("Марсель", population=861000, budget=1200000)
city5 = City("Берлин", population=3759000, budget=2500000)

county1 = County("Район A1", budget=1000000)
county2 = County("Район B1", budget=1500000)
county3 = County("Район C1", budget=2000000)

county1.add_city(city1)
county1.add_city(city2)
county2.add_city(city3)
county2.add_city(city4)
county3.add_city(city5)

estonia.add_county(county1)
france.add_county(county2)
germany.add_county(county3)

person1 = Person("Иван", 30, 50000, "Мужской")
person2 = Person("Мария", 25, 60000, "Женский")
person3 = Person("Петр", 40, 55000, "Мужской")
person4 = Person("vasya", 18,25000, "mees")
city1.add_resident(person1)
city1.add_resident(person2)
city2.add_resident(person3)

person1.pay_taxes(city1)
person2.pay_taxes(city1)
person3.pay_taxes(city2)

city1.request_funding(10000, county1)
city3.request_funding(20000, county2)

# Сбор налогов
county1.collect_taxes()
county2.collect_taxes()
county3.collect_taxes()

estonia.collect_taxes()
france.collect_taxes()
germany.collect_taxes()

person1.move_to_city(city3)
person2.move_to_city(city4)


print(city1.info())
print(city2.info())
print(city3.info())
print(city4.info())
print(city5.info())

print(county1.info())
print(county2.info())
print(county3.info())

print(estonia.info())
print(france.info())
print(germany.info())

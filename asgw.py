class Laptop:
    def __init__(self, brand, ram, storage, year, model):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.year = year
        self.model = model

    def update_laptop(self, ram_updated, storage_updated=0, year_updated=0):
        if ram_updated > 0:
            self.ram = ram_updated
        if storage_updated > 0:
            self.storage = storage_updated
        if year_updated > 0:
            self.year = year_updated

    def check_age(self):
        current_year = 2025 
        age = current_year - self.year
        if age > 5:
            return "Этот ПК старше 5 лет, и следует его выкинуть"
        else:
            return f"Этот ПК {age} года, его можно оставить"
    def display_info(self): 
        print(f"Бренд: {self.brand}, Модель: {self.model}")
        print(f": {self.brand}, Модель: {self.model}")
        print(f"Бренд: {self.brand}, Модель: {self.model}")
    
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

 class Organization:
    def __init__(self, name):
        self.name = name
        self.employees = []
   def (self):
        return f"{self.name} - {self.position}"


    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        for employee in self.employees:
            print(employee)

legion = Laptop("Lenovo", 16, 512, 2012, "XP13")

print("До обновления характеристик:")
print(legion.check_age())

legion.update_laptop(ram_updated=32, storage_updated=1024)

print("\nПосле обновления характеристик:")
print(legion.check_age())

org = Organization("TechCorp")

org.add_employee(Employee("Иван Александрович", "Менеджер"))
org.add_employee(Employee("Мария Петрова", "Разработчик"))
org.add_employee(Employee("Сергей Пидоров", "Тестировщик"))

print("\nСотрудники организации:")
org.show_employees()


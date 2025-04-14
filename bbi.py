import random

# Базовый класс
class Component:
    def __init__(self, model, brand, power):
        self.model = model
        self.brand = brand
        self.power = power

    def get_info(self):
        raise NotImplementedError()

    def run_diagnostics(self):
        raise NotImplementedError()

class GPU(Component):
    def __init__(self, model, brand, power, vram, has_driver):
        super().__init__(model, brand, power)
        self.vram = vram
        self.has_driver = has_driver
        self.status = ""

    def get_info(self):
        return f"GPU: {self.model} by {self.brand}, VRAM: {self.vram} GB"

    def run_diagnostics(self):
        if not self.has_driver or self.vram < 2:
            self.status = "Проблема: драйвер не установлен или мало памяти"
            return False
        temp = random.randint(40, 100)
        if temp > 85:
            self.status = f"Проблема: перегрев ({temp}°C)"
            return False
        self.status = "GPU в порядке"
        return True

class RAM(Component):
    def __init__(self, model, brand, power, usage_percent):
        super().__init__(model, brand, power)
        self.usage = usage_percent
        self.status = ""

    def get_info(self):
        return f"RAM: {self.model} by {self.brand}, использование: {self.usage}%"

    def run_diagnostics(self):
        if self.usage > 95:
            self.status = "Проблема: память почти заполнена"
            return False
        self.status = "RAM в порядке"
        return True

class Storage(Component):
    def __init__(self, model, brand, power, size_gb, read_speed):
        super().__init__(model, brand, power)
        self.size = size_gb
        self.read_speed = read_speed
        self.status = ""

    def get_info(self):
        return f"Storage: {self.model} by {self.brand}, {self.size} GB, скорость: {self.read_speed} MB/s"

    def run_diagnostics(self):
        if self.read_speed < 100:
            self.status = "Проблема: медленное чтение"
            return False
        self.status = "Storage в порядке"
        return True

gpu = GPU("GTX 1660", "NVIDIA", 120, 6, True)
ram = RAM("Corsair", "Corsair", 50, 60)
storage = Storage("Samsung SSD", "Samsung", 10, 512, 550)

components = [gpu, ram, storage]

for comp in components:
    print(comp.get_info())
    if comp.run_diagnostics():
        print("Диагностика: OK")
    else:
        print("Диагностика:", comp.status)
    print("-" * 40)


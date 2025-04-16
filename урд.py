class Level:
    def __init__(self, level_number, initial_resources, min_resources):
        self.level_number = level_number 
        self.resources = initial_resources  
        self.min_resources = min_resources  
        self.is_active = True  

    def get_resources(self):
        """Метод получения ресурсов на этом уровне"""
        return self.resources if self.is_active else 0

    def distribute_resources(self):
        """Метод для принятия решения, как распределить ресурсы"""
        if not self.is_active:
            return

        print(f"\nУровень {self.level_number}:")
        print(f"Доступные ресурсы: {self.resources}")
        decision = input("Выберите действие (1 - оставить себе, 2 - передать на следующий уровень): ")

        if decision == '1':
            print(f"Уровень {self.level_number} оставляет ресурсы себе.")
        elif decision == '2':
            transfer_amount = int(input("Сколько ресурсов передать на следующий уровень? "))
            self.transfer_resources(transfer_amount)
            print(f"Уровень {self.level_number} передает {transfer_amount} ресурсов на следующий уровень.")
        else:
            print("Некорректный выбор.")

        self.check_if_active()

    def transfer_resources(self, amount):
        """Передача ресурсов следующему уровню"""
        if amount <= self.resources:
            self.resources -= amount
            print(f"Передано {amount} ресурсов.")
        else:
            print(f"Недостаточно ресурсов для передачи {amount}.")

    def check_if_active(self):
        """Проверка, достаточно ли ресурсов для выживания уровня"""
        if self.resources < self.min_resources:
            self.is_active = False
            print(f"Уровень {self.level_number} вышел из игры из-за недостатка ресурсов.")
    
class Game:
    def __init__(self, num_levels=10):
        self.levels = []
        self.num_levels = num_levels
        self.create_levels()

    def create_levels(self):
        """Создание уровней с фиксированными характеристиками"""
        for i in range(self.num_levels):
            initial_resources = 100 
            min_resources = 30 
            self.levels.append(Level(i + 1, initial_resources, min_resources))

    def play(self):
        """Основной игровой процесс"""
        while any(level.is_active for level in self.levels):
            for level in self.levels:
                if level.is_active:
                    level.distribute_resources()
            print("\nПроверка текущего состояния:")
            self.print_game_state()

    def print_game_state(self):
        """Вывод состояния всех уровней"""
        for level in self.levels:
            status = "Активен" if level.is_active else "Вышел из игры"
            print(f"Уровень {level.level_number}: {status}, Ресурсы: {level.resources}")
        print("\n")

if __name__ == "__main__":
    game = Game()
    game.play()


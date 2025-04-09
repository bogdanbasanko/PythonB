from datetime import datetime

class Event:
    def __init__(self, note, officer_name):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.note = note
        self.officer_name = officer_name

    def __str__(self):
        return f"[{self.timestamp}] {self.officer_name}: {self.note}"

class Case:
    def __init__(self, case_id, description):
        self.case_id = case_id
        self.description = description
        self.status = "open"
        self.events = []

    def add_event(self, event):
       
        if isinstance(event, Event):
            self.events.append(event)
        else:
            raise TypeError("Добавляемый объект должен быть экземпляром класса Event")

    def close_case(self):
        self.status = "closed"

    def get_timeline(self):
        return [str(e) for e in self.events]

    def get_status(self):
        return self.status

    def get_description(self):
        return self.description

    def get_case_id(self):
        return self.case_id


class PoliceOfficer:
    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number
        self.cases = []

    def assign_case(self, case):
        self.cases.append(case)

    def get_case_by_id(self, case_id):
        for case in self.cases:
            if case.get_case_id() == case_id:
                return case
        raise ValueError(f"Дело с ID {case_id} не найдено.")

    def get_summary(self):
        total = len(self.cases)
        closed = sum(1 for case in self.cases if case.get_status() == "closed")
        return f"Всего: {total} | Закрыто: {closed} | Открыто: {total - closed}"

    def get_info(self):
        return f"Имя: {self.name}, Номер: {self.badge_number}"

officer1 = PoliceOfficer("Дмитрий Коваленко", "1001")
officer2 = PoliceOfficer("Сергей Машара", "5678")


case1 = Case(101, "Кража телефона")
case2 = Case(102, "Угон автомобиля")

officer1.assign_case(case1)
officer2.assign_case(case2)


event1 = Event("Осмотр места происшествия", officer1.name)
event2 = Event("Опрос свидетелей", officer1.name)
case1.add_event(event1)
case1.add_event(event2)

print("Timeline для дела 101:", case1.get_timeline())

print("Сводка для офицера 1:", officer1.get_summary())

print("Информация об офицере 1:", officer1.get_info())

try:
    officer1.get_case_by_id(102)  
except ValueError as e:
    print(e)

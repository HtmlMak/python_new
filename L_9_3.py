class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom = {'wage':wage, 'bonus':bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self, name, surname):
        print(f'Полное имя: {self.name} {self.surname}')

    def get_total_incom(self, _incom):
        print(f"Общий доход составляет {self._incom['wage'] + self._incom['bonus']} рублей")

worker_1 = Position('Иван', 'Петров', 'инженер', 100000, 30000)
worker_1.get_full_name(worker_1.name, worker_1.surname)
worker_1.get_total_incom(worker_1._incom)

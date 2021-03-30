class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"{self.title} пишет")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"{self.title} рисует")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"{self.title} выделяет текст")

pen_blue = Stationery('Ручка')
pen_blue.draw()
pen_black = Pen('Ручка')
pen_black.draw()
pencil_red = Pencil('Карандаш')
pencil_red.draw()
handle_yellow = Handle('Маркер')
handle_yellow.draw()

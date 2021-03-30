class TrafficLight:
    color = []

    def running(self):
        color = ['красный', 'желтый', 'зеленый']
        print(f'{color[0]} горит 7 секунд, {color[1]} горит 2 секунды, {color[2]} горит 15 секунд')

t = TrafficLight()
t.running()

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asfflt_weight(self, _length, _width):
        print(f'Необходимое количество асфальта {_length*_width*25*5/1000} тонн')

road_5_km = Road(7000, 20)
road_5_km.asfflt_weight(road_5_km._length, road_5_km._width)
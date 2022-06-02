from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume,(int, float)):  # инициализировать объект "Стакан"
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume # объем жидкости


if __name__ == "__main__":
    glass1 = Glass(200,120)  # инициализировать два объекта типа Glass
    galss2 = Glass(500,50)
    print(glass1)

    glass3 = (-220, 20)# попробовать инициализировать не корректные объекты
    glass4 = (100, 2000)

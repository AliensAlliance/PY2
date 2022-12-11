import doctest
from typing import Union


class Wardrobe:
    def __init__(self, empty_shelves: int, amount_of_items: int):
        """
        Создание и подготовка к работе объекта "Шкаф"

        :param empty_shelves: Количество пустых полок
        :param amount_of_items: Количество вещей в шкафу (одна вещь занимает одну полку)

        Примеры:
        >>> wardrobe = Wardrobe(10, 0)  # инициализация экземпляра класса
        """
        if not isinstance(empty_shelves, int):
            raise TypeError("Количество пустых полок должно быть типа int")
        if not empty_shelves > 0:
            raise ValueError("Количество пустых полок должно быть положительным числом")
        self.empty_shelves = empty_shelves

        if not isinstance(amount_of_items, int):
            raise TypeError("Количество вещей должно быть типа int")
        if amount_of_items < 0:
            raise ValueError("Количество вещей не может быть отрицательным числом")
        self.amount_of_items = amount_of_items

    def is_wardrobe_empty(self) -> bool:
        """
        Функция которая проверяет является ли шкаф пустым

        :return: Является ли шкаф пустым

        Примеры:
        >>> wardrobe = Wardrobe(10, 0)
        >>> wardrobe.is_wardrobe_empty()
        """
        ...

    def put_item_in_wardrobe(self, items: int) -> None:
        """
        В шкаф кладут вещи.

        :param items: Количество добавляемых вещей
        :raise ValueError: Если количество добавляемых превышает количество пустых полок, то вызываем ошибку

        Примеры:
        >>> wardrobe = Wardrobe(10, 0)
        >>> wardrobe.put_item_in_wardrobe(6)
        """
        if not isinstance(items, int):
            raise TypeError("Количество добавляемых вещей должно быть типа int")
        if items < 0:
            raise ValueError("Количество добавляемых вещей должно быть положительным числом")
        ...

    def get_item_out_of_wardrobe(self, necessary_items) -> None:
        """
        Извлечение вещей из шкафа.

        :param necessary_items: Количество нужных вещей
        :raise ValueError: Если количество нужных вещей превышает количество лежащих в шкафу вещей,
        то возвращается ошибка.

        :return: Количество реально извлеченных вещей

        Примеры:
        >>> wardrobe = Wardrobe(10, 10)
        >>> wardrobe.get_item_out_of_wardrobe(5)
        """
        ...


class Bus:
    def __init__(self, empty_seats: int, occupied_seats: int):
        """
        Создание и подготовка к работе объекта "Автобус"

        :param empty_seats: Количество не занятых мест в автобусе
        :param occupied_seats: Количество занятых мест

        Примеры:
        >>> bus = Bus(10, 5)  # инициализация экземпляра класса
        """
        if not isinstance(empty_seats, int):
            raise TypeError("Количество пустых мест должно быть типа int")
        if not empty_seats > 0:
            raise ValueError("Количество пустых мест должно быть положительным числом")
        self.empty_seats = empty_seats

        if not isinstance(occupied_seats, int):
            raise TypeError("Количество занятых мест должно быть типа int")
        if occupied_seats < 0:
            raise ValueError("Количество занятых мест не может быть отрицательным числом")
        self.occupied_seats = occupied_seats

    def is_bus_empty(self) -> bool:
        """
        Функция которая проверяет является ли автобус пустым

        :return: Является ли автобус пустым

        Примеры:
        >>> bus = Bus(10, 0)
        >>> bus.is_bus_empty()
        """
        ...

    def people_get_on_bus(self, number_of_people: int) -> None:
        """
        Люди садятся в автобус.

        :param number_of_people: Количество зашедших в автобус людей

        :raise ValueError: Если количество зашедших в автобус людей превышает количество свободных мест в автобусе,
        то вызываем ошибку

        Примеры:
        >>> bus = Bus(10, 0)
        >>> bus.people_get_on_bus(5)
        """
        if not isinstance(number_of_people, int):
            raise TypeError("Количество людей, которые садятся в автобус, должно быть типа int")
        if number_of_people < 0:
            raise ValueError("Количество людей, которые садятся в автобус, должно быть не отрицательным числом")
        ...

    def people_get_off_bus(self, vacant_seats) -> None:
        """
        Люди выходят из автобуса.

        :param vacant_seats: Количество освободившихся мест
        :raise ValueError: Если количество освободившихся мест превышает количество занятых мест,
        то возвращается ошибка.

        :return: Количество реально освободившихся мест

        Примеры:
        >>> bus = Bus(10, 10)
        >>> bus.people_get_off_bus(5)
        """
        ...


class RiceCooker:
    def __init__(self, capacity_volume: Union[int, float], amount_of_rice: Union[int, float], amount_of_water: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Рисоварка"

        :param capacity_volume: Объем рисоварки
        :param amount_of_rice: Количество риса в рисоварке
        :param amount_of_water: Количество воды в рисоварке

        Примеры:
        >>> rice_cooker = RiceCooker(1000, 200, 400)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем рисоварки должнен быть типа int или float")
        if not capacity_volume > 0:
            raise ValueError("Объем рисоварки должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(amount_of_rice, (int, float)):
            raise TypeError("Количество риса должно быть типа int или float")
        if amount_of_rice < 0:
            raise ValueError("Количество риса не может быть отрицательным числом")
        self.amount_of_rice = amount_of_rice

        if not isinstance(amount_of_water, (int, float)):
            raise TypeError("Количество воды должно быть типа int или float")
        if amount_of_water < 0:
            raise ValueError("Количество воды не может быть отрицательным числом")
        self.amount_of_water = amount_of_water

    def is_rice_cooker_empty(self) -> bool:
        """
        Функция которая проверяет пустая ли рисоварка

        :return: Является ли рисоварка пустой

        Примеры:
        >>> rice_cooker = RiceCooker(1000, 0, 0)
        >>> rice_cooker.is_rice_cooker_empty()
        """
        ...

    def add_rice_to_rice_cooker(self, rice: Union[int, float]) -> None:
        """
        Добавление риса в рисоварку.

        :param rice: Количество добавляемого риса

        :raise ValueError: Если количество добавляемого риса превышает свободное место в рисоварке,
        то вызываем ошибку

        Примеры:
        >>> rice_cooker = RiceCooker(1000, 200, 0)
        >>> rice_cooker.add_rice_to_rice_cooker(100)
        """
        if not isinstance(rice, (int, float)):
            raise TypeError("Количество добавляемого риса должно быть типа int или float")
        if rice < 0:
            raise ValueError("Количество добавляемого риса должно быть не отрицательным числом")
        ...

    def add_water_to_rice_cooker(self, water: Union[int, float]) -> None:
        """
        Добавление воды в рисоварку.

        :param water: Количество добавляемой воды

        :raise ValueError: Если количество добавляемой превышает свободное место в рисоварке,
        то вызываем ошибку

        Примеры:
        >>> rice_cooker = RiceCooker(1000, 200, 100)
        >>> rice_cooker.add_water_to_rice_cooker(100)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Количество добавляемой воды должно быть типа int или float")
        if water < 0:
            raise ValueError("Количество добавляемой воды должно быть не отрицательным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass

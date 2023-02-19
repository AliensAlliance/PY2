from typing import Union


class Tea:
    def __init__(self, tea_type: str, origin: str):
        """
        Базовый класс Чай

        :param tea_type: тип чая (черный, зеленый и т.п.)
        :param origin: происхождение чая

        Примеры:
        >>> some_tea = Tea('зеленый', 'Шри-Ланка')
        """
        self.tea_type = tea_type
        self.origin = origin

    def __str__(self) -> str:
        """
        Печатный вид экземпляра класса
        """
        return f"Чай {self.tea_type}. Происхождение {self.origin}"

    def __repr__(self) -> str:
        """
        Вид экземпляра класса при применении repr()
        """
        return f"{self.__class__.__name__}(leaf_type={self.tea_type!r}, origin={self.origin!r})"

    def tea_brewing(self, temperature: int, amount_of_tea: Union[int, float]) -> None:
        """
        Нагревание воды до нужной температуры и заваривание чая
        Публичный метод

        :param temperature: температура заваривания чая
        :param amount_of_tea: количество завариваемого чая
        """

    def tea_serving(self) -> None:
        """
        Пьем чай
        Публичный метод
        """


class LeafTea(Tea):
    def __init__(self, tea_type: str, origin: str, mass_of_tea: Union[int, float]):
        """
        Дочерний класс Листовой чай

        :param tea_type: тип чая
        :param origin: происхождение чая
        :param mass_of_tea: количество грамм чая для заваривания
        """
        super().__init__(tea_type, origin)
        self.mass_of_tea = mass_of_tea

    def __repr__(self) -> str:
        """
        Вид экземпляра класса при применении repr()
        Перегрузка метода базового класса
        """
        return f"{self.__class__.__name__}(tea_type={self.tea_type!r}, origin={self.origin!r}, mass_of_tea={self.mass_of_tea!r})"

    def tea_brewing(self, temperature: int, amount_of_tea: Union[int, float]) -> None:
        """
        Завариваем некоторое количество грамм листового чая, поэтому перегружаем метод базового класса
        Публичный метод

        :param temperature: температура заваривания
        :param amount_of_tea: количество чая, измеряемое в граммах
        """


class TeaInBags(Tea):
    """ Дочерний класс Чай в пакетиках"""

    def __init__(self, tea_type: str, origin: str, number_of_teabags: int):
        super().__init__(tea_type, origin)
        self.number_of_teabags = number_of_teabags

    def __repr__(self) -> str:
        """
        Вид экземпляра класса при применении repr()
        Перегрузка метода базового класса
        """
        return f"{self.__class__.__name__}(tea_type={self.tea_type!r}, origin={self.origin!r}, number_of_teabags={self.number_of_teabags!r})"

    def tea_brewing(self, temperature: int, amount_of_tea: Union[int, float]) -> None:
        """
        Завариваем пакетики чая, поэтому перегружаем метод базового класса
        Публичный метод

        :param temperature: температура заваривания
        :param amount_of_tea: количество чая, измеряемое в пакетиках
        """


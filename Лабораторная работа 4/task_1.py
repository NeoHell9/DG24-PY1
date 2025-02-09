class RZD:
    """ 
    Базовый класс для всех типов поездов РЖД.
    Содержит основные атрибуты и методы, общие для всех поездов.
    """

    def __init__(self, number: str, route: str, max_speed: int):
        """
        Инициализация базового класса.

        :param number: Номер поезда
        :param route: Маршрут следования
        :param max_speed: Максимальная скорость (км/ч)
        """
        self._number = number  # Номер поезда, инкапсуляция для защиты от изменения
        self.route = route
        self.max_speed = max_speed

    @property
    def number(self) -> str:
        """Геттер номера поезда (изменение запрещено)"""
        return self._number

    def __str__(self) -> str:
        return f"Поезд {self.number}, маршрут: {self.route}, макс. скорость: {self.max_speed} км/ч."

    def __repr__(self) -> str:
        return f"RZD(number={self.number!r}, route={self.route!r}, max_speed={self.max_speed})"

    def get_train_info(self) -> str:
        """Возвращает информацию о поезде."""
        return f"Поезд {self.number} следует по маршруту {self.route}."


class FreightTrain(RZD):
    """
    Класс грузового поезда, наследуется от RZD.
    Добавляет информацию о грузоподъемности.
    """

    def __init__(self, number: str, route: str, max_speed: int, capacity: int):
        """
        Инициализация грузового поезда.

        :param number: Номер поезда
        :param route: Маршрут следования
        :param max_speed: Максимальная скорость (км/ч)
        :param capacity: Грузоподъемность (тонн)
        """
        super().__init__(number, route, max_speed)
        self.capacity = capacity

    def __str__(self) -> str:
        return f"{super().__str__()} Грузоподъемность: {self.capacity} тонн."

    def __repr__(self) -> str:
        return f"FreightTrain({super().__repr__()}, capacity={self.capacity})"

    def get_train_info(self) -> str:
        """
        Переопределенный метод get_train_info.
        У грузовых поездов важна информация о грузе, поэтому метод дополнен.
        """
        return f"Грузовой поезд {self.number}, маршрут: {self.route}, перевозит до {self.capacity} тонн груза."


class PassengerTrain(RZD):
    """
    Класс пассажирского поезда, наследуется от RZD.
    Добавляет информацию о количестве мест.
    """

    def __init__(self, number: str, route: str, max_speed: int, seats: int):
        """
        Инициализация пассажирского поезда.

        :param number: Номер поезда
        :param route: Маршрут следования
        :param max_speed: Максимальная скорость (км/ч)
        :param seats: Количество мест
        """
        super().__init__(number, route, max_speed)
        self.seats = seats

    def __str__(self) -> str:
        return f"{super().__str__()} Количество мест: {self.seats}."

    def __repr__(self) -> str:
        return f"PassengerTrain({super().__repr__()}, seats={self.seats})"

    def get_train_info(self) -> str:
        """
        Переопределенный метод get_train_info.
        Для пассажирских поездов важно количество мест, поэтому добавляем эту информацию.
        """
        return f"Пассажирский поезд {self.number}, маршрут: {self.route}, вместимость: {self.seats} пассажиров."
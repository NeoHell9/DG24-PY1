import doctest

class Table:
    def __init__(self, length: float, width: float, material: str):
        """
        Создание и подготовка к работе объекта "Стол"

        :param length: Длина стола в сантиметрах
        :param width: Ширина стола в сантиметрах
        :param material: Материал, из которого сделан стол

        Примеры:
        >>> table = Table(120, 60, 'wood')
        """
        if not isinstance(length, (int, float)) or length <= 0:
            raise ValueError("Длина стола должна быть положительным числом")
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Ширина стола должна быть положительным числом")
        if not isinstance(material, str) or not material:
            raise TypeError("Материал должен быть непустой строкой")

        self.length = length
        self.width = width
        self.material = material

    def get_area(self) -> float:
        """
        Вычислить площадь стола.

        :return: Площадь стола в квадратных сантиметрах

        Примеры:
        >>> table = Table(120, 60, 'wood')
        >>> table.get_area()
        7200.0
        """
        return self.length * self.width

    def describe(self) -> str:
        """
        Описание стола.

        :return: Строка с описанием стола

        Примеры:
        >>> table = Table(120, 60, 'wood')
        >>> table.describe()
        'Table made of wood, 120x60 cm.'
        """
        return f"Table made of {self.material}, {self.length}x{self.width} cm."


class Tree:
    def __init__(self, species: str, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева
        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах

        Примеры:
        >>> tree = Tree('Oak', 5.0, 10)
        """
        if not isinstance(species, str) or not species:
            raise TypeError("Вид дерева должен быть непустой строкой")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст дерева должен быть неотрицательным числом")

        self.species = species
        self.height = height
        self.age = age

    def grow(self, years: int) -> None:
        """
        Увеличить высоту дерева в зависимости от возраста.

        :param years: Количество лет роста

        Примеры:
        >>> tree = Tree('Oak', 5.0, 10)
        >>> tree.grow(5)
        """
        if not isinstance(years, int) or years < 0:
            raise ValueError("Количество лет должно быть неотрицательным числом")
        self.height += years * 0.5
        self.age += years

    def describe(self) -> str:
        """
        Описание дерева.

        :return: Строка с описанием дерева

        Примеры:
        >>> tree = Tree('Oak', 5.0, 10)
        >>> tree.describe()
        'Oak tree, 5.0 meters tall, 10 years old.'
        """
        return f"{self.species} tree, {self.height} meters tall, {self.age} years old."


class SocialMedia:
    def __init__(self, name: str, user_count: int):
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Название социальной сети
        :param user_count: Количество пользователей

        Примеры:
        >>> sm = SocialMedia('Facebook', 1000000)
        """
        if not isinstance(name, str) or not name:
            raise TypeError("Название должно быть непустой строкой")
        if not isinstance(user_count, int) or user_count < 0:
            raise ValueError("Количество пользователей должно быть неотрицательным числом")

        self.name = name
        self.user_count = user_count

    def add_user(self, count: int) -> None:
        """
        Добавить пользователей.

        :param count: Количество добавляемых пользователей

        Примеры:
        >>> sm = SocialMedia('Facebook', 1000000)
        >>> sm.add_user(500)
        """
        if not isinstance(count, int) or count <= 0:
            raise ValueError("Количество добавляемых пользователей должно быть положительным числом")
        self.user_count += count

    def describe(self) -> str:
        """
        Описание социальной сети.

        :return: Строка с описанием

        Примеры:
        >>> sm = SocialMedia('Facebook', 1000000)
        >>> sm.describe()
        'Facebook has 1000000 users.'
        """
        return f"{self.name} has {self.user_count} users."


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

# продублировала целиком данные по классу House из module_5_2
class House:  # зададим класс House
    def __init__(self, name, number_of_floors): # определим метод __init__ с названием и кол-вом этажей
        # присвоим атрибутам названия и кол-ва этажей атрибуты
        self.name = name
        self.number_of_floors = number_of_floors

    # вызвать метод __len__ чтобы определить номер эт.
    # (передача целого числа представляет кол-во эт., далее нам нужно будет для типа данных)
    def __len__(self):
        return self.number_of_floors

    # вызвать метод __str__ чтобы вывести ин-цию о доме
    # закладываем строковое значение
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"



    # одинаковое ли ко-во эт.
    def __eq__(self, other):
        if isinstance(other, House):  # проверка типа значение: other к типу House
            return self.number_of_floors == other.number_of_floors
        return False # иначе возврат False

    # у self эт. меньше чем у other
    def __lt__(self, other):
        if isinstance(other, House):  # проверка типа значение: other к типу House
            return self.number_of_floors < other.number_of_floors
        return False # иначе возврат False

    # у self эт. меньше или равно чем у other
    def __le__(self, other):
        if isinstance(other, House):  # проверка типа значение: other к типу House
            return self.number_of_floors <= other.number_of_floors
        return False # иначе возврат False

    # у self эт. больше чем у other
    def __gt__(self, other):
        if isinstance(other, House):  # проверка типа значение: other к типу House
            return self.number_of_floors > other.number_of_floors
        return False # иначе возврат False

    # у self эт. больше или равно чем у other
    def __ge__(self, other):
        if isinstance(other, House):  # проверка типа значение: other к типу House
            return self.number_of_floors >= other.number_of_floors
        return False # иначе возврат False
    # self эт. не равно other
    def __ne__(self, other):
        if isinstance(other, House):  # проверка типа значение: other к типу House
            return self.number_of_floors != other.number_of_floors
        return False # иначе возврат False


    # увеличивает кол-во этажей на переданное значение value
    def __add__(self, value):
        if isinstance(value, int):  # проверка типа значение: целое ли число value
            return House(self.name, self.number_of_floors + value)  # вернет нам название и увеличенное кол-во эт.
        return False # иначе возврат False

    def __radd__(self, value):
        if isinstance(value, int):  # проверка типа значение: целое ли число value
            return House(self.name, self.number_of_floors + value)
        return False # иначе возврат False

    def __iadd__(self, value):
        if isinstance(value, int):  # проверка типа значение: целое ли число value
            self.number_of_floors += value   # увелич. кол-во эт. на value
            return self # возвращает сам объект self
        return False # иначе возврат False

# Пример выполняемого кода
home1 = House('ЖК Лазурные небеса', 37)
home2 = House('ЖК АртСити', 10)

print(home1)
print(home2)

print(home1 == home2)  # __eq__
print(home1 < home2)  # __lt__
print(home1 <= home2)  # __le__
print(home1 > home2)  # __gt__
print(home1 >= home2)  # __ge__
print(home1 != home2)  # __ne__

home1 = home1 + -27  # __add__
print(home1)
print(home1 == home2)

home1 += 3  # __iadd__
print(home1)

home2 = 37 + home2  # __radd__
print(home2)

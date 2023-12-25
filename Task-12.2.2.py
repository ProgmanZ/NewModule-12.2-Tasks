class Human:
    __count = 1

    def __init__(self, human_name, human_age):
        self.__setter_name(human_name)
        self.__setter_age(human_age)
        Human.__count += 1

    def __setter_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception("Ошибка в Имени. Ожидается ввод строчного значения.")

    def __setter_age(self, age):
        if isinstance(age, int):
            if age in range(0, 100):
                self.__age = age
            else:
                raise Exception("Ошибка в возрасте. Возраст может быть значением от 0 до 100.")
        else:
            raise Exception("Возраст должен быть числовым значением.")

    def __getter_name(self):
        return self.__name

    def __getter_age(self):
        return self.__age

    def __str__(self):
        return f"\nЧеловек: \n\tИмя:{self.__getter_name()}, " \
               f"\n\tВозраст: {self.__getter_age()}, " \
               f"\n\nВсего человек: {Human.__count}"


human_men = Human("Анатолий", 45)
human_woman = Human("Светлана", 43)

print(human_men, human_woman)

human_men._Human__age = 3
print(human_men)

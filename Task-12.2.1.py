class Point:
    __count = 1

    def __init__(self, x_coord=0, y_coord=0):
        self.__setter_x(x_coord)
        self.__setter_y(y_coord)
        self.__number = Point.__count
        Point.__count += 1

    def __setter_x(self, x):
        if isinstance(x, int):
            self.__x_coord = x
        else:
            raise Exception("Ошибка для координаты X !!! Ожидается ввод только цифр...")

    def __setter_y(self, y):
        if isinstance(y, int):
            self.__y_coord = y
        else:
            raise Exception("Ошибка для координаты Y !!! Ожидается ввод только цифр...")

    def __getter_x(self):
        return self.__x_coord

    def __getter_y(self):
        return self.__y_coord

    def __str__(self):
        return f"Точка имеет координаты x:{self.__getter_x()} y:{self.__getter_y()}\n " \
               f"Точка имеет номер: {self.__number}\n"


point_1 = Point(-4, 6)
point_2 = Point(46, 55)


print(point_1)
print(point_2)

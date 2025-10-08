import turtle


def draw_inward_spiral():
    # Настройки окна и черепашки
    screen = turtle.Screen()
    screen.setup(width=900, height=900)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Максимальная скорость рисования
    t.penup()  # Поднимаем перо, чтобы переместиться в начальную точку без рисования

    # Начальные координаты для спирали снаружи внутрь
    # Начинаем с верхнего левого угла, чтобы первый ход был влево
    start_x = 100
    start_y = 100
    t.goto(start_x, start_y)
    t.pendown()  # Опускаем перо, чтобы начать рисовать

    segment_length = 500  # Начальная длина сегмента
    direction = 0  # 0: влево, 1: вниз, 2: вправо, 3: вверх
    decrement = 20  # Величина уменьшения длины

    while segment_length > 0:
        if direction == 0:  # Влево
            t.setheading(180)  # Поворот влево
            t.forward(segment_length)

        elif direction == 1:  # Вниз
            t.setheading(270)  # Поворот вниз
            t.forward(segment_length)

        elif direction == 2:  # Вправо
            t.setheading(0)  # Поворот вправо
            t.forward(segment_length)

        elif direction == 3:  # Вверх
            t.setheading(90)  # Поворот вверх
            t.forward(segment_length)

        # Уменьшаем длину после каждой линии.
        segment_length -= decrement

        # Следующее направление
        direction = (direction + 1) % 4

        # Если сегмент стал слишком коротким, выходим из цикла
        if segment_length <= 0:
            # Коррекция конечного направления - влево
            if direction != 0:  # если текущее направление не влево, то сделать последний поворот
                t.setheading(180)  # устанавливаем влево
            break

    turtle.done()


# Запускаем функцию для рисования спирали
draw_inward_spiral()

# Refactored main.py


class Unit:
    def __init__(self, state: str, field, speed: float = 1):
        self.x = float(0)
        self.y = float(0)
        self.state = state
        self.speed = speed
        self.field = field

    def __repr__(self):
        return f'X: {self.x}\n' \
               f'Y: {self.y}'

    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        elif self.state == 'walk':
            return self.speed
        else:
            raise ValueError('Недопустимое состояние')

    def move(self, direction):
        speed = self._get_speed()

        if direction == "UP":
            self.field.set_unit(x=self.x, y=self.y + speed, unit=self)
        elif direction == "DOWN":
            self.field.set_unit(x=self.x, y=self.y - speed, unit=self)
        elif direction == "LEFT":
            self.field.set_unit(x=self.x - speed, y=self.y, unit=self)
        elif direction == "RIGHT":
            self.field.set_unit(x=self.x + speed, y=self.y, unit=self)


class Field:
    def __init__(self):
        self.x_length = 10
        self.y_length = 20

    def set_unit(self, x: int, y: int, unit: Unit):
        if x > self.x_length or y > self.y_length:
            raise ValueError("Сюда нельзя идти")
        elif x < 0 or y < 0:
            raise ValueError("Сюда нельзя идти")

        unit.x = x
        unit.y = y


if __name__ == "__main__":
    field_1 = Field()
    unit_1 = Unit(state="fly", field=field_1)
    print(unit_1)
    unit_1.move(direction='RIGHT')
    unit_1.move(direction='UP')
    print(unit_1)

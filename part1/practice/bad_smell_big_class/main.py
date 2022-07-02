# Refactored main.py


class Warrior:
    def move(self):
        pass

    def attack(self):
        pass

    def defense(self):
        pass


class Healer:
    def move(self):
        pass

    def defense(self):
        pass

    def heal(self, unit: object):
        pass


class Tree:
    def defense(self):
        pass

    def on_fire(self):
        pass


class Trap:
    def attack(self):
        pass


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()
    tree = Tree()

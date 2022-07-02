# Refactored main.py


class Person:
    def __init__(self, room_num: int, city_population: int):
        self.room_num = room_num
        self.city_population = city_population

    def get_person_room(self):
        return self.room_num

    def get_city_population(self):
        return self.city_population


if __name__ == '__main__':
    person = Person(room_num=42, city_population=9001)
    print(person.get_person_room())
    print(person.get_city_population())

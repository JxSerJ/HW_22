# Refactored main.py


csv_data = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(csv):
    data = {key: value for key, value in {entry.split(';')[0]: entry.split(';')[1] for entry in csv.split('\n')}.items()}
    return data


def _sort(data: dict) -> dict:
    data_sorted = {key: value for key, value in sorted(data.items(), key=lambda x: int(x[1]))}
    return data_sorted


def _filter(data: dict):
    data_filtered = {key: value for key, value in data.items() if int(value) > 10}
    return data_filtered


def get_users_list(csv: str):
    data = _filter(_sort(_read(csv)))
    data_compiled = [{"name": name, "age": int(age)} for name, age in data.items()]
    return data_compiled


if __name__ == '__main__':
    print(get_users_list(csv_data))

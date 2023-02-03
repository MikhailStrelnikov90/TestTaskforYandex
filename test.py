import pytest


def delivery_cost_calculation(cost_delivery):
    if cost_delivery < 400:
        cost_delivery = 400
    return cost_delivery


def input_distance():
    distance = None
    while True:
        try:
            print("Введите расстояние доставки в км: ", end='')
            distance = int(input())
            if distance <= 0:
                print("Введено некорректное значение расстояния")
                continue
            else:
                break
        except ValueError:
            print("Введено некорректное значение расстояния")
            continue
    return distance


def delivery_cost_with_distance(distance):
    distance = int(distance)
    cost_delivery = 0
    if distance > 30:
        cost_delivery += 300
    elif 10 < distance <= 30:
        cost_delivery += 200
    elif 2 < distance <= 10:
        cost_delivery += 100
    elif 0 < distance <= 2:
        cost_delivery += 50
    return cost_delivery


def input_dimensions():
    while True:
        print("Введите габариты груза (допустимые значения 'большие' или 'маленькие'): ", end='')
        dimensions = input()
        if dimensions not in ['большие', "маленькие"]:
            print("Введено некорректное значение габаритов(допустимые значения 'большие' или 'маленькие')")
            continue
        else:
            return dimensions


def delivery_cost_with_dimensions(dimensions, cost_with_distance):
    cost_delivery = cost_with_distance
    dimensions = dimensions
    if dimensions == "большие":
        cost_delivery += 200
    elif dimensions == "маленькие":
        cost_delivery += 100
    return cost_delivery


def input_fragility(distance):
    while True:
        print("Введите значение, если груз хрупкий (допустимое значения 'хрупкий', если груз нехрупкий, то оставьте поле пустым): ", end='')
        fragility = input()
        if fragility not in ["хрупкий", ""]:
            print("Введено некорректное значение хрупкости груза(допустимое значения 'хрупкий', если груз нехрупкий, то оставьте поле пустым)")
            continue
        elif fragility == "хрупкий" and distance > 30:
            print("Хрупкие грузы нельзя возить на расстояние более 30 км")
            continue
        else:
            return fragility


def delivery_cost_with_fragility(fragility, distance, cost_with_distance_and_dimensions):
    cost_delivery = cost_with_distance_and_dimensions
    if fragility == "хрупкий" and distance <= 30:
        cost_delivery += 300
    return cost_delivery


def input_workload():
    while True:
        print("Введите значение загруженности службы доставки (допустимое значения 'очень высокая', 'высокая', 'повышенная', 'другое'): ", end='')
        workload = input()
        if workload not in ['очень высокая', 'высокая', 'повышенная', 'другое']:
            print("Введено некорректное значение загруженности службы доставки(допустимое значения 'очень высокая', 'высокая', 'повышенная', 'другое')")
            continue
        else:
            return workload


def delivery_cost_with_workload(workload, cost_with_distance_demensions_and_fragility):
    cost_delivery = float(cost_with_distance_demensions_and_fragility)
    if workload == 'очень высокая':
        cost_delivery *= 1.6
    elif workload == 'высокая':
        cost_delivery *= 1.4
    elif workload == 'повышенная':
        cost_delivery *= 1.2
    return cost_delivery


def test_calculation_cost_with_distance():
    assert delivery_cost_with_distance(31) == 300, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_distance(30) == 200, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_distance(11) == 200, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_distance(10) == 100, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_distance(3) == 100, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_distance(2) == 50, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_distance(0) == 0, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_distance(-1) == 0, "Неверно рассчитывается стоимость доставки"


def test_calculation_cost_with_distance_and_dimensions():
    assert delivery_cost_with_dimensions("большие", 300) == 500, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_dimensions("большие", 0) == 200, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_dimensions("маленькие", 300) == 400, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_dimensions("маленькие", 0) == 100, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_dimensions("123", 0) == 0, "Неверно рассчитывается стоимость доставки"


def test_calculation_cost_with_distance_dimensions_and_fragility():
    assert delivery_cost_with_fragility("хрупкий", 30, 500) == 800, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_fragility("хрупкий", 31, 500) == 500, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_fragility("", 30, 500) == 500, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_fragility("123", 1, 500) == 500, "Неверно рассчитывается стоимость доставки"


def test_calculation_cost_with_distance_dimensions_fragility_and_workload():
    assert delivery_cost_with_workload('очень высокая', 800) == 1280.0, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_workload('высокая', 500) == 700.0, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_workload('повышенная', 100) == 120.0, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_workload('другое', 100) == 100.0, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_with_workload('123', 800) == 800.0, "Неверно рассчитывается стоимость доставки"


def test_calculation_cost_with_all_parameters():
    assert delivery_cost_calculation(399) == 400, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_calculation(400) == 400, "Неверно рассчитывается стоимость доставки"
    assert delivery_cost_calculation(401) == 401, "Неверно рассчитывается стоимость доставки"


def main():
    distance_value = input_distance()
    cost_delivery_with_distance = delivery_cost_with_distance(distance_value)
    dimensions_value = input_dimensions()
    cost_delivery_with_distance_and_demensions = delivery_cost_with_dimensions(dimensions=dimensions_value, cost_with_distance=cost_delivery_with_distance)
    fragility_value = input_fragility(distance_value)
    cost_delivery_with_distance_demensions_and_fragility = delivery_cost_with_fragility(fragility=fragility_value, distance=distance_value, cost_with_distance_and_dimensions=cost_delivery_with_distance_and_demensions)
    workload_value = input_workload()
    cost_delivery_with_all_parameters = delivery_cost_with_workload(workload=workload_value, cost_with_distance_demensions_and_fragility=cost_delivery_with_distance_demensions_and_fragility)
    print(delivery_cost_calculation(cost_delivery=cost_delivery_with_all_parameters))


if __name__ == "__main__":
    main()

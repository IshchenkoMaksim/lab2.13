#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def show_commands():
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить маршрут;")
    print("list - вывести список маршрутов;")
    print("select - нати маршруты по времени")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def get_route(routes):
    """
    Запросить данные о маршруте.
    """
    destination = input("Пункт назначения? ")
    number = input("Номер поезда? ")
    time = input("Время отправления?(формат чч:мм) ")

    route = {
        'destination': destination,
        'number': number,
        'time': time
    }
    routes.append(route)
    if len(routes) > 1:
        routes.sort(key=lambda item: item.get('destination', ''))


def display_routes(way):
    """
    Отобразить список маршрутов.
    """
    if way:
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 30,
            '-' * 4,
            '-' * 20
        )
        print(line)
        print(
            '| {:^30} | {:^4} | {:^20} |'.format(
                "Пункт назначения",
                "№",
                "Время"
            )
        )
        print(line)

        for route in way:
            print(
                '| {:<30} | {:>4} | {:<20} |'.format(
                    route.get('destination', ''),
                    route.get('number', ''),
                    route.get('time', '')
                )
            )
        print(line)

    else:
        print("Маршруты не найдены")


def select_routes(way, period):
    """
    Выбрать маршруты после заданного времени.
    """
    result = []

    for route in way:
        time_route = tuple(route.get('time').split(':'))
        if period < time_route:
            result.append(route)

    # Возвратить список выбранных маршрутов.
    return result

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from pack_ind2 import show_commands, get_route, display_routes, select_routes


if __name__ == '__main__':
    routes = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            get_route(routes)

        elif command == 'list':
            display_routes(routes)

        elif command == 'select':
            time_select = tuple(input("Выберите время отправления"
                                      "(формат чч:мм): ").split(':'))
            selected = select_routes(routes, time_select)
            display_routes(selected)

        elif command == 'help':
            show_commands()

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

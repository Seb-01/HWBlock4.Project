from django.core.management.base import BaseCommand, CommandError
from CityRouters.models import Station, Route
import csv

class Command(BaseCommand):
    help = 'Загрузка данных из scv файла'

    def add_arguments(self, parser):
        # Парсер наследуется от argparse.ArgumentParser, и про аргументы, принимаемые функцией add_argument,
        # можно почитать в документации к библиотеке argparse в документации python

        # получаем один неименованный аргумент (dest='args')
        # nargs=1 - количество аргументов
        parser.add_argument(nargs=1, type=str, dest='args', help='Имя файла с json данными')


    # требуется аргумент - имя файла, например так:
    # python manage.py insert_data_from_json <jsonfile name>
    def handle(self, *args, **options):

        with open(*args, 'rt') as csv_file:
            header = []
            routes = []
            table_reader = csv.reader(csv_file, delimiter=';')

            for table_row in table_reader:
                if not header:
                    header = {idx: value for idx, value in enumerate(table_row)}
                else:
                    row = {header.get(idx) or 'col{:03d}'.format(idx): value
                           for idx, value in enumerate(table_row)}

                    # сюда отдельно маршруты выписываем
                    routes=row['RouteNumbers'].split(';')

                    result=Station(
                                    name=row['Name'],
                                    latitude=row['Latitude_WGS84'],
                                    longitude=row['Longitude_WGS84'],
                                   )
                    result.save()

                    # маршруты разбираем
                    #exist_route=Route.objects.values_list('name',flat=True)
                    exist_route = list(Route.objects.values_list('name', flat=True))
                    #exist_route = Route.objects.all()

                    # перебираем маршруты по этой остановке из csv
                    for route in routes:
                        # если такой маршрут уже существует в БД
                        if route in exist_route:
                            # получаем из БД этот маршут и ...
                            route_from_db=Route.objects.get(name=route)
                            # ... добавляем его в эту остановку
                            result.routes.add(route_from_db)

                        else:
                            # такого маршрута еще нет в БД - добавляем в БД и ...
                            new_route=Route(name=route)
                            new_route.save()

                            # ... добавляем его в эту остановку
                            result.routes.add(new_route)


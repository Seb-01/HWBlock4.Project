from django.template import library

register = library.Library()


def get_routes(qs):
    routes_str='Маршруты: '
    for route in qs:
        routes_str+=route.name + ' '
    return routes_str

register.filter('get_routes', get_routes)
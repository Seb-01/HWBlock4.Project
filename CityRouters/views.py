from django.shortcuts import render

from CityRouters.models import Station, Route


def stations_view(request):
    template = 'stations.html'

    class MapPoint:
        x=55.7522
        y=37.6156

    routes = Route.objects.all()

    #Что пришло в запросе (есть ли параметры):
    route_str=request.GET.get('route')
    stations_list=[]

    if route_str:
        route_rec = Route.objects.get(name=route_str)
        stations = Station.objects.prefetch_related('routes').filter(routes=route_rec)

        for station in stations:
            stations_list.append([station.latitude,station.longitude])
    else:
        stations=''


    staions_num=len(stations_list)
    if staions_num > 1:

        start = MapPoint()
        start.x=stations_list[0][0]
        start.y=stations_list[0][1]

        finish = MapPoint()
        finish.x = stations_list[staions_num-1][0]
        finish.y = stations_list[staions_num-1][1]

        center = MapPoint()
        center.x= str((start.x+finish.x) / 2)
        center.y = str((start.y + finish.y) / 2)
    else:
        center = MapPoint()

    print(center.x, center.y)

    context = {
            'routes': routes,
            'stations': stations,
            'center': center
    }
    result = render(request, template, context)

    return result



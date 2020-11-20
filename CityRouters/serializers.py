from rest_framework import serializers
from CityRouters.models import Station


class StationSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = Station
        fields = ('id', 'name', 'latitude', 'longitude', 'routes')

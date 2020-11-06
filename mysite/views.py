from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mysite.models import *
from mysite.serializers import *

@api_view(['GET'])
def location_from_locode(request, key):
    try:
        location = Location.objects.get(LOCODE=key)
    except Location.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LocationSerializer(location)
        return Response(serializer.data)

@api_view(['GET'])
def location_from_namewodiacritics(request, key):
    try:
        locations = Location.objects.filter(NameWoDiacritics__contains=key)
    except Location.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
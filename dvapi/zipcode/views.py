import logging
from logging import raiseExceptions
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Zipcode
from .serializers import ZipcodeSerializer
from .services import ZipcodeService

logger = logging.getLogger(__name__)

class ZipcodeView(
    APIView,
    UpdateModelMixin,
    DestroyModelMixin,
):

    def get(self, request, id=None):
        if id:
            
            try:
                queryset = Zipcode.objects.get(id=id)
            except Zipcode.DoesNotExist:
                return Response({'errors': 'This zipcode does not exist'}, status=404)
            
            read_serializer = ZipcodeSerializer(queryset)

        return Response(read_serializer.data)

    def post(self, request):
        create_serializer = ZipcodeSerializer(data=request.data)


        if create_serializer.is_valid(raise_exception=True):
            zipcode_object = create_serializer.save()

            read_serializer = ZipcodeSerializer(zipcode_object)

            return Response(read_serializer.data, status=201)
    
        return Response(create_serializer.errors, status=400)
    
    def delete(self, request, id=None):
        try:
            zipcode = Zipcode.objects.get(id=id)
        except Zipcode.DoesNotExist:
            # If the zipcode does not exist, return an error response
            return Response({'errors': 'This zipcode does not exist.'}, status=400)

        zipcode.delete()

        return Response(status=204)

class ZipcodeSearchView(
    APIView,
):
    def get(self, request, zipcode=None):
        logger.info('method get by zipcode called')
        if zipcode:
                filteredZipcodes = ZipcodeService.get_zipcodes(zipcode=zipcode)
        else:
            return Response({'errors': 'Missing zipcode on the request'}, status=400)
            
            #deactivated serializer to match api response from challenge
            #read_serializer = ZipcodeSerializer(queryset, many=True)

        return Response(filteredZipcodes)


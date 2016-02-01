from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import viewsets

from .serializers import UserSerializer


class EnthusiastViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


    @detail_route()
    def city(self, request, pk):
        """
        Returns the city of the user
        :param request:
        :return:
        """
        user = self.get_object()
        return Response({'city': self.get_object().enthusiast.city})

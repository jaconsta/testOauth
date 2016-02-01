from django.shortcuts import render
from rest_framework import viewsets

from .models import Name
from .serializers import NameSerializer

# Create your views here.
class NameViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Names methods
	"""
	queryset = Name.objects.all()
	serializer_class = NameSerializer
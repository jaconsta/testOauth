from .models import Name
from rest_framework import serializers


class NameSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Name
        fields = ('name', )


from rest_framework import serializers
from main.models import Team


class TeamSerializer(serializers.ModelSerializer):
    """
    We declare this class for Serializing and deserializing a object with Django
    Rest Framework. We inherit from ModelSerializer avoid writing repetitive
    code and we have the save and update method by default ready to use.
    """
    class Meta:
        model = Team
        fields = ('name',)


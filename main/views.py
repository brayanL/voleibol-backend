from datetime import datetime

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from main.serializers import TeamSerializer
from .models import Match


class StartGame(viewsets.ViewSet):
    """
    Allows to register teams, by default a new match is also saved.
    Return created teams and match id.
    """
    @action(methods=['post'], detail=False, name='Start Game')
    def insert(self, request):
        serializer = TeamSerializer(data=request.data, many=True)
        if serializer.is_valid():
            teams = serializer.save()
            match = Match.objects.create(date=datetime.today().isoformat())
            teams_list = [({"id": team.id, "name": team.name}) for team in teams]
            return Response({"teams": teams_list, "match": match.id}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from datetime import datetime

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from main.serializers import TeamSerializer, MatchDetailSerializer
from .models import Match


class StartGame(viewsets.ViewSet):
    @action(methods=['post'], detail=False, name='Start Game')
    def start(self, request):
        """
        Allows to register teams, by default a new match is also saved.
        Return created teams and match id.
        """
        serializer = TeamSerializer(data=request.data, many=True)
        if serializer.is_valid():
            teams = serializer.save()
            match = Match.objects.create(date=datetime.today().isoformat())
            teams_list = [({"id": team.id, "name": team.name}) for team in teams]
            return Response({"teams": teams_list, "match": match.id}, status=status.HTTP_200_OK)
        print('Serializer Errors: ', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False, name='Add Set')
    def add_set(self, request):
        """
        Add a new Set to Current Game.
        """
        serializer = MatchDetailSerializer(data=request.data, many=True)
        print("Request Data: ", request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




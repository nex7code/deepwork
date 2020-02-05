from rest_framework import status, permissions, viewsets
from dork.models import WorkBoard
from dork.serializers import WorkBoardSerializer


class WorkBoardViewSet(viewsets.ModelViewSet):
    queryset = WorkBoard.objects.all()
    serializer_class = WorkBoardSerializer
    permission_classes = [permissions.AllowAny]


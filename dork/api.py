from rest_framework import status, permissions, viewsets
from dork.models import WorkBoard
from dork.serializers import WorkBoardSerializer


class WorkBoardViewSet(viewsets.ModelViewSet):
    serializer_class = WorkBoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.workboards.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

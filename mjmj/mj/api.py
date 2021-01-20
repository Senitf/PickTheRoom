from mj.models import Condition
from rest_framework import viewsets, permissions
from .serializers import ConditionSerializer

# Condition Viewset
class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ConditionSerializer
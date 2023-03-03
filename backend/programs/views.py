from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import permissions
from .serializers import WellnessProgramSerializer
from .models import WellnessProgram

class WellnessProgramListview(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = WellnessProgram.objects.all()
    serializer_class = WellnessProgramSerializer
    pagination_class = None

class WellnessProgramView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = WellnessProgram.objects.all()
    serializer_class = WellnessProgramSerializer

class ActiveView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = WellnessProgram.objects.filter(is_active=True)
    serializer_class = WellnessProgramSerializer
    pagination_class = None
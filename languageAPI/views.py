from rest_framework import generics
from .serializers import LanguageSerializer, ParadigmSerializer
from rest_framework.permissions import IsAuthenticated

from .models import Language, Paradigm

class LanguageList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ParadigmsList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer
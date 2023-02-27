from rest_framework import generics
from .serializers import LanguageSerializer, ParadigmSerializer

from .models import Language, Paradigm

class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ParadigmsList(generics.ListCreateAPIView):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer
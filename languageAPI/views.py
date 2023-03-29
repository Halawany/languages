from rest_framework import generics, viewsets
from .serializers import LanguageViewSetSerializer, ParadigmViewSetSerializer
from rest_framework.permissions import IsAuthenticated

from .models import Language, Paradigm


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageViewSetSerializer

class ParadigmViewSet(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmViewSetSerializer
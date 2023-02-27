from rest_framework import generics
from .serializers import LanguageSerializer

from .models import Language

class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
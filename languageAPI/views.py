from rest_framework import generics
from .serializers import LanguageSerializer, ParadigmSerializer, LanguageActionsSerializer
from rest_framework.permissions import IsAuthenticated

from .models import Language, Paradigm

class LanguageList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class  LanguageUpdateOrDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = LanguageActionsSerializer

    def get_queryset(self):
        return Language.objects.filter(pk=self.kwargs["pk"])
    

class ParadigmsList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer
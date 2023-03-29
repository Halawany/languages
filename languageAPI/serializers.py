from rest_framework import serializers

from .models import Language, Paradigm

class LanguageViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"

class ParadigmViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields = "__all__"
from rest_framework import serializers

from .models import Language, Paradigm

class ParadigmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields = '__all__'
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name', 'creator', 'created_at', 'paradigm', 'description']
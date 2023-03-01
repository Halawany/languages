from django.contrib import admin

from .models import Language, Paradigm

admin.site.register(Paradigm)
admin.site.register(Language)
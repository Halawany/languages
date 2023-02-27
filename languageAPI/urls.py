from django.urls import path

from .views import LanguageList, ParadigmsList

urlpatterns = [
    path('languages/', LanguageList.as_view(),),
    path('paradigms/', ParadigmsList.as_view(),),
]

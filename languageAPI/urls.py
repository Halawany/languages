from django.urls import path

from .views import LanguageList, ParadigmsList, LanguageUpdateOrDestroy

urlpatterns = [
    path('', LanguageList.as_view(),),
    path('paradigms/', ParadigmsList.as_view(),),
    path('language/<int:pk>', LanguageUpdateOrDestroy.as_view(), ),
]

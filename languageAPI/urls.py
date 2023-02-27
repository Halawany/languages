from django.urls import path

from .views import LanguageList

urlpatterns = [
    path('v1', LanguageList.as_view(),)
]

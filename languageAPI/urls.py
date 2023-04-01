from rest_framework import routers

from .views import LanguageViewSet, ParadigmViewSet

router = routers.SimpleRouter()
router.register(r'language', LanguageViewSet, basename="languages")
router.register(r'paradigm', ParadigmViewSet, basename="paradigms")
urlpatterns = router.urls
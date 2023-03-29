from rest_framework import routers

from .views import LanguageViewSet, ParadigmViewSet

router = routers.SimpleRouter()
router.register(r'language', LanguageViewSet)
router.register(r'paradigm', ParadigmViewSet)
urlpatterns = router.urls
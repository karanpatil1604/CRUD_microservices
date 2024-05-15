from rest_framework.routers import DefaultRouter
from api.views import DictionaryViewSet

router = DefaultRouter()
router.register("dictionaries", DictionaryViewSet, basename="dictionaries")

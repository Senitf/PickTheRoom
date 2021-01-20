from rest_framework import routers
from .api import ConditionViewSet

router = routers.DefaultRouter()
router.register('api/conditions', ConditionViewSet, 'conditions')

urlpatterns = router.urls
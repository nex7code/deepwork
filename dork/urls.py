from rest_framework import routers
from dork.api import ProjectViewSet

router = routers.DefaultRouter()
router.register("api/dork", ProjectViewSet, "ListView")
urlpatterns = router.urls

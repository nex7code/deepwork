from rest_framework import routers
from dork.api import WorkBoardViewSet

router = routers.DefaultRouter()
router.register("api/dork", WorkBoardViewSet, "WorkBoardView")
urlpatterns = router.urls

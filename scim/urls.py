from rest_framework.routers import SimpleRouter
from .views import ScimAppViewset

router = SimpleRouter()
router.register('scim', ScimAppViewset)

urlpatterns = router.urls
from rest_framework.routers import SimpleRouter
from .views import NewUserModelViewSet

router = SimpleRouter()

router.register('user', NewUserModelViewSet)

urlpatterns = [
]
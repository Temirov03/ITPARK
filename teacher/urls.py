from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TeacherViewSet,TeacherDeatilView


router = SimpleRouter()

router.register('teacher', TeacherViewSet)


urlpatterns = [
    path("<int:id>/",TeacherDeatilView.as_view(),name='self1')
]
from django.urls import path
from .views import index, ParkViewSet, about, contact, course, team, testimonial, message,\
    message1, message2,message3,index1,message4,message5,CBVListView
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register('itpark', ParkViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('index1/', index1,name='index1'),
    path('about/',about, name='about'),
    path('contact/',contact, name="contact"),
    path('course/', course,name="course"),
    path('team/',team,name="team"),
    path('testimonial/', testimonial,name="testimonial"),
    path('message/',message,name="message"),
    path('message1/',message1,name="message1"),
    path("message2/", message2, name="message2"),
    path("message3/",message3, name="message3"),
    path('message4',message4,name="message4"),
    path("message5/",message5,name="message5"),
    path("<int:pk>/", CBVListView.as_view(), name="self1")
]

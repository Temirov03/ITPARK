from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Teacher
from .serializer import TeacherSerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.

class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDeatilView(DetailView):
    template_name = 'self.html'
    model = Teacher

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Teacher, id=id_)

from django.shortcuts import render, redirect
from .serializer import ParkSerializer
from rest_framework.viewsets import ModelViewSet
from teacher.models import Teacher
from user.models import NewUser
from user.form import NewUserForm
from .models import Park
from django.views.generic import DetailView


# Create your views here.


def index(request):
    img = Teacher.objects.all()
    coment = NewUser.objects.all()
    park = Park.objects.all()
    context = {
        'img': img,
        'coment': coment,
        'park': park
    }
    return render(request, "index.html", context)


def index1(request):
    return render(request, "index1.html")


def about(request):
    park = Park.objects.all()
    context = {
        "park": park
    }
    return render(request, "about.html", context)


def course(request):
    return render(request, "courses.html")


def contact(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        form.save()
        return redirect('index')
    else:
        form = NewUserForm()

    return render(request, "contact.html", {"form": form})


def team(request):
    return render(request, "team.html")


def testimonial(request):
    return render(request, "testimonial.html")


def message(request):
    return render(request, "message.html")


def message1(request):
    return render(request, "message1.html")


def message2(request):
    return render(request, "message2.html")


def message3(request):
    return render(request, "message3.html")


def message4(request):
    return render(request, "message4.html")


def message5(request):
    return render(request, "message5.html")


class CBVListView(DetailView):
    queryset = Teacher.objects.all()
    template_name = "detail.html"

    def get_context_data(self,*args, **kwargs):
        context = super(CBVListView,self).get_context_data(**kwargs)
        context['model'] = "model"
        return context


class ParkViewSet(ModelViewSet):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer

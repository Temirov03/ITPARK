from django.shortcuts import render, redirect
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializer import NewUserSerializer
from .models import  NewUser
from rest_framework.views import APIView


# Create your views here.
#
# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserCreateAPIView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDeleteAPIView(APIView):
#
#     def delete(self, request, pk):
#         obj = User.objects.filter(pk=pk)
#         obj.delete()
#         return Response("Bu ma'lumot o'chib ketdi !!!")


class NewUserModelViewSet(ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer


class NewUserAPIView(APIView):
    template_name = 'contact.html'

    def post(self, request):
        serializer = NewUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("index")
        else:
            return redirect("contact")



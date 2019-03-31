import django_filters
from rest_framework import viewsets, filters, generics
from rest_framework.response import Response

from .models import User
from .serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class SignUpViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        User.objects.create(user_id=request.POST['user_id'], password=request.POST['password'], nickname=request.POST['user_id'])
        return Response({
            "message": "Account successfully created",
            "user": {
                "user_id": request.POST['user_id'],
                "nickname": request.POST['user_id']
                }
            })

class

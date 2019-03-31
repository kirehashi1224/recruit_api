import django_filters
from rest_framework import viewsets, filters, generics
from rest_framework.response import Response
from django.core.exceptions import ValidationError

from .models import User
from .serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SignUpViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        user = User(user_id=request.POST['user_id'], password=request.POST['password'],
                    nickname=request.POST['user_id'])
        try:
            user.full_clean()
        except ValidationError as e:
            return Response(status=400, data={"message": "Account creation failed", "cause": "required user_id and password"})

        user.save()

        return Response({
            "message": "Account successfully created",
            "user": {
                "user_id": request.POST['user_id'],
                "nickname": request.POST['user_id']
                }
            })


class CloseViewSet(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        # request.auth.
        # User.objects.filter(name)
        user = User(user_id=request.POST['user_id'], password=request.POST['password'], nickname=request.POST['user_id'])
        if not user:
            Response(status=401, data={"message":"Authentication Faild"})

        return Response({
            "message": "Account and user successfully removed",
        })

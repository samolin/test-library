from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from .tasks import send_welcome_email

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user_id = response.data.get('id')
        send_welcome_email.delay(user_id)
        return response

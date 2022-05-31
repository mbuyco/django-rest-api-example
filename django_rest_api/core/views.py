from django.contrib.auth.models import User
from django_rest_api.core.serializers import UserRegistrationSerializer
from django_rest_api.core.services.registration_service import RegistrationService
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    registration_service = RegistrationService()
    user = registration_service.register(serializer.data)
    return Response(user)

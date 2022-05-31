from django.contrib.auth.models import Group
from django_rest_api.core.models import User
from django_rest_api.core.serializers import GroupSerializer
from django_rest_api.core.serializers import UserRegistrationSerializer
from django_rest_api.core.serializers import UserSerializer
from django_rest_api.core.services.registration_service import RegistrationService
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def register(request):
    """
    API endpoint to register a user
    """
    serializer = UserRegistrationSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    registration_service = RegistrationService()
    registration_service.register(serializer.data)
    return Response({
        'user': serializer.data,
        'errors': [],
    }, status.HTTP_201_CREATED)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing/managing users
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

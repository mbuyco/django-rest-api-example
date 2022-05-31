from django.contrib.auth.models import User


class RegistrationService:
    """
    Class for handling user registration business logic
    """
    def register(self, data):
        user = User()
        user.username = data['email']
        user.email = data['email']
        user.first_name = data.get('first_name', '')
        user.last_name = data.get('last_name', '')
        user.is_active = False
        return user.save()

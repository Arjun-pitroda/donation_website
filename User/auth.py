from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class AuthenticationEmailBackend(ModelBackend):
    def authenticate(request,self, username=None, password=None, **kwargs):

        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if getattr(user, 'is_active', False) and user.check_password(password):
                return user
        return None

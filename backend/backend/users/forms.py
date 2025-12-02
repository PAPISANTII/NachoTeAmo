from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    template_name = "users/user_registration_form_snippet.html"
    
    class Meta:
        model = User
        fields = ("username", "email",)
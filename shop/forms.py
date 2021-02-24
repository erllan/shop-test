from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]

    def save(self, commit=True):
        user = User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'],
                                        password=self.cleaned_data['password1'])
        user.is_active = False
        user.save()
        return user

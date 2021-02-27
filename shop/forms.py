from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.core.mail import send_mail
from django.template import loader
from uuid import uuid4


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.is_active = False
        user.set_password(self.cleaned_data["password1"])
        key = uuid4()
        user.key = key
        if commit:
            user.save()

        html_message = loader.render_to_string(
            'email/confirim.html', {'key': key}
        )
        message = ''
        send_mail(subject='вы зарегестрировались на нашем сайте', message=message, html_message=html_message,
                  from_email=None,
                  recipient_list=[self.cleaned_data['email']],
                  fail_silently=False)

        return user


class ChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

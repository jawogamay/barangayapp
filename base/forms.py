from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User,Report


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email','phone_number', 'password1', 'password2']


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        exclude = ['user', 'status']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio', 'phone_number']
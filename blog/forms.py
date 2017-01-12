from django.forms import ModelForm
from models import UserInfo


class RegisterForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'

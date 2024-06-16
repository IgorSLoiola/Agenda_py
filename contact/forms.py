from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class contactForm(forms.ModelForm):
    # photo = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/*',}))
    class Meta:
        model = Contact
        fields = ('name','phone', 'email', 'description', 'category', 'photo')

    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')

        if name == '[0-9_]':
            self.add_error('name', ValidationError('Não pode coloca valor numerico', code='invalid'))

        return super().clean()

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError('Já existe este E-mail', code='invalid'))
            return email

class loginUser(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class registerUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
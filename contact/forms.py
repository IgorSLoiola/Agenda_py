from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class contactForm(forms.ModelForm):
    photo = forms.ImageField(required=False, widget=forms.FileInput(attrs={'accept': 'image/*',}))
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
    first_name = forms.CharField(
        min_length=2,
        max_length=55,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': ''
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=55,
        required=False,
        help_text='Required.',
        error_messages={
            'min_length': ''
        }
    )
    password1 = forms.CharField(
        label='password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    password2 = forms.CharField(
        label='Confirm the Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        password = self.cleaned_data.get('password1')
        user = super().save(commit=False)
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 or password2:
            if password1 != password2:
                self.add_error('password2', ValidationError('As senha nao sao iguais.'))
        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error('email', ValidationError('Já existe este E-mail', code='invalid'))

            return email
    def clean_password(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as e:
                self.add_error('password1', ValidationError(e))
        return password1
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    profile_img = forms.ImageField()
    userBio = forms.CharField(widget=forms.Textarea(), max_length=1000)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})
        self.fields['userBio'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tell us about yourself'})
        self.fields['profile_img'].widget.attrs.update({'style': 'display:none;', 'id':'profile_img'})

    class Meta:
        model = User
        fields = ('username', 'email', 'profile_img', 'password1', 'password2', 'userBio', )
        widgets = {
            'userBio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your Password'}),
            
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
        }
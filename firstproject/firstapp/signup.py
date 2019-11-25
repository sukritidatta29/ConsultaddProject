from django import forms
from django.core import validators
from . models import SignUpForm, Post


class SignupForm(forms.ModelForm):
    '''firstname=forms.CharField(label="First Name")
    lastname = forms.CharField(label="Last Name")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    repassword = forms.CharField(label="Re-Enter Password", widget=forms.PasswordInput)'''

    def clean(self):
        password=self.cleaned_data['password']
        rpassword = self.cleaned_data['repassword']
        if password!=rpassword:
            raise forms.ValidationError("Passwords Do not match! Please Check Again")
        if len(password)<4:
            raise forms.ValidationError("Password should be atlest 4 characters long!")


    class Meta:
        model=SignUpForm
        fields="__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
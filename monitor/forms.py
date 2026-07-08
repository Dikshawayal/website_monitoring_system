from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Website


# ==========================
# Custom Login Form
# ==========================
class CustomAuthenticationForm(AuthenticationForm):

    error_messages = {
        "invalid_login": "Username or Password is incorrect.",
        "inactive": "This account is inactive.",
    }

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:

            UserModel = get_user_model()

            if not UserModel.objects.filter(username=username).exists():
                raise forms.ValidationError(
                    "Username not found.",
                    code="invalid_login"
                )

            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password
            )

            if self.user_cache is None:
                raise forms.ValidationError(
                    "Password is incorrect.",
                    code="invalid_login"
                )

            self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


# ==========================
# Signup Form
# ==========================
class SignupForm(UserCreationForm):

    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your full name"
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email"
        })
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Choose a username"
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Create password"
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirm password"
        })
    )

    class Meta:
        model = User
        fields = (
            "full_name",
            "email",
            "username",
            "password1",
            "password2",
        )

    def save(self, commit=True):

        user = super().save(commit=False)

        names = self.cleaned_data["full_name"].split()

        user.first_name = names[0]

        if len(names) > 1:
            user.last_name = " ".join(names[1:])

        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user


# ==========================
# Website Form
# ==========================
class WebsiteForm(forms.ModelForm):

    class Meta:
        model = Website

        fields = [
            "name",
            "url",
            "description",
        ]

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter website name"
            }),

            "url": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://example.com"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Enter description"
            }),
        }


# ==========================
# Password Change Form
# ==========================
class CustomPasswordChangeForm(PasswordChangeForm):

    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter current password"
        })
    )

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter new password"
        })
    )

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirm new password"
        })
    )

    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2
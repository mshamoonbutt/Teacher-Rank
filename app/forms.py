from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        allowed_domains = ['formanite.fccollege.edu.pk', 'fccollege.edu.pk']
        domain = email.split('@')[-1]
        
        if domain not in allowed_domains:
            raise forms.ValidationError(
                "Please use an email address from @formanite.fccollege.edu.pk or @fccollege.edu.pk"
            )
        return email 
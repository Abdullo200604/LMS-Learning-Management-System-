from django import forms
from django.contrib.auth import authenticate

class CustomLoginForm(forms.Form):
    login = forms.CharField(label="Login yoki email", max_length=255)
    password = forms.CharField(label="Parol", widget=forms.PasswordInput)

    def clean(self):
        login = self.cleaned_data.get('login')
        password = self.cleaned_data.get('password')
        from django.contrib.auth import get_user_model
        User = get_user_model()
        user = None

        # login orqali qidiramiz (email yoki username)
        try:
            user_obj = User.objects.get(email=login)
        except User.DoesNotExist:
            try:
                user_obj = User.objects.get(username=login)
            except User.DoesNotExist:
                user_obj = None

        if user_obj is not None:
            user = authenticate(username=user_obj.email, password=password)  # username maydoni = email!
        else:
            user = None

        if not user:
            raise forms.ValidationError("Login yoki parol noto‘g‘ri!")
        self.user = user
        return self.cleaned_data
from django import forms #スーパーユーザーが管理画面でデータを入力できるように準備。
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Password再入力', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
    def clean(self): # ここでconfirm_passwordが正しいかどうかを確認する。
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('パスワードが一致しません')

    def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    website = forms.URLField(required=False)
    picture = forms.FileField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_staff', 'is_active', 'is_superuser', 'website', 'picture')
    
    def clean_password(self):
        # すでに登録されているパスワードを返す
        return self.initial['password']


class RegistForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('パスワードが異なります')

    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user) # パスワードが正しいかを確認している。
        user.set_password(self.cleaned_data['password'])
        user.save() # パスワードを保存して次の行でそのユーザーの情報として返す。
        return user

class LoginForm(forms.Form):
    email = forms.CharField(label="メールアドレス")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput())

class UserEditForm(forms.ModelForm): 
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')

    class Meta:
        model = User
        fields = ('username', 'email')

class PasswordChangeForm(forms.ModelForm):

    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('password', )
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('パスワードが異なります')

    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


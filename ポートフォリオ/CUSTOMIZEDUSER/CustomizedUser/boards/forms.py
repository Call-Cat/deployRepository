from django import forms
from .models import Memos


class CreateMemoForm(forms.ModelForm):
    title = forms.CharField(label='タイトル')

    class Meta:
        model = Memos
        fields = ('title',)


class DeleteMemoForm(forms.ModelForm):

    class Meta:
        model = Memos
        fields = []

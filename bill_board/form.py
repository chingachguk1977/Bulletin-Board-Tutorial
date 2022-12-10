from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Advert, Resp


class AdvertForm(forms.ModelForm):
    """
    Adding a new post
    """
    text = forms.CharField(label='Advertisement body', widget=CKEditorUploadingWidget())
    error_css_class = 'text-danger fw-semibold'

    class Meta:
        model = Advert
        fields = ('title', 'text', 'category', 'attach',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'attach': forms.FileInput(attrs={'class': 'form-control'}),
        }


class RespForm(forms.ModelForm):
    """
    Adding a response to a post
    """
    error_css_class = 'text-danger fw-semibold'

    class Meta:
        model = Resp
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }

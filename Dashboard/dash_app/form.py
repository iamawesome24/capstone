from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    files = forms.FileField(upload_to='Dashboard\media', widget=forms.ClearableFileInput(attrs={'multiple': True}))

from django import forms
from .models import CleanedFile


class UploadExcelForm(forms.ModelForm):
    class Meta:
        model = CleanedFile
        fields = ['excel_file']
        labels = {'excel_file': 'انتخاب فایل اکسل'}
        widgets = {
            'excel_file': forms.FileInput(attrs={'class': 'form-control'})
            
        }

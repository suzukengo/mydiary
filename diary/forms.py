from django import forms
from .models import Diary

#ModelFormクラスを継承

class DiaryForm(forms.ModelForm):
    class Meta:
        model=Diary
        fields=('date','title','text',)
    

from django import forms
from .models import Diary

#ModelFormクラスを継承

class DiaryForm(forms.ModelForm):
    class Meta:
        model=Diary
        fields=('date','title','text',)
        #widgetは辞書型のデータを持っている。
        widgets={
            'date':forms.DateInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.TextInput(attrs={'class':'form-control'}),
        }
    

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView

from .forms import DiaryForm

# Create your views here.
#TemplateViewはDjango特有のクラスを継承している。Viewを作成するための汎用的なビュー。汎用的な処理を返せるView
class IndexView(TemplateView):
    template_name='index.html'

class DiaryCreateView(CreateView):
    template_name='diary_create.html'
    #form_classは入力フォームを上記ファイル内で入力可能にする
    form_class=DiaryForm
    #入力フォームを投降後に遷移するurl
    #reverse_lazyはurlを遅延評価するメソッド
    success_url = reverse_lazy('diary:diary_create_complete')

class DiaryCreateCompleteView(TemplateView):
    template_name='diary_create_complete.html'
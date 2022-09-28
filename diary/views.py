from datetime import timezone

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Diary
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

class DiaryListView(ListView):
    template_name='diary_list.html'
    model=Diary

#DetailViewはデータの詳細画面を作成するために便利なクラス
class DiaryDetailView(DetailView):
    template_name='diary_detail.html'
    model=Diary

class DiaryUpdateView(UpdateView):
    template_name='diary_update.html'
    model=Diary
    fields=('date','title','text')
    success_url=reverse_lazy('diary:diary_list')

    def form_valid(selfself,form):
        diary=form.save(commit=False)

        diary.save()
        return super().form_valid(form)

class DiaryDeleteView(DeleteView):
    template_name='diary_delete.html'
    model=Diary
    success_url=reverse_lazy('diary:diary_list')
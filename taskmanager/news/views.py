from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})
    
class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_news.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author

class NewsDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author
    
@login_required 
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'news/create.html', data)
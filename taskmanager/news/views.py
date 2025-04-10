from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Articles
from .forms import ArticlesForm
from django.contrib import messages

def home(request):
    featured_news = Articles.objects.filter(is_featured=True).order_by('-date')
    latest_news = Articles.objects.order_by('-date')
    return render(request, 'news/home.html', {
        'featured_news': featured_news,
        'latest_news': latest_news,
    })

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

def news_details(request, id):
    article = Articles.objects.get(id=id)
    return render(request, 'news/details_news.html', {'article': article})

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, 'Статья успешно добавлена!')
            return redirect('news_home')
        else:
            messages.error(request, 'Ошибка при добавлении статьи.')
    else:
        form = ArticlesForm()
    return render(request, 'news/create.html', {'form': form})

@login_required
def news_update(request, id):
    article = Articles.objects.get(id=id)
    if request.user != article.author:
        messages.error(request, 'У вас нет прав для редактирования этой статьи.')
        return redirect('news_home')
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья успешно обновлена!')
            return redirect('news-detail', id=article.id)
        else:
            messages.error(request, 'Ошибка при обновлении статьи.')
    else:
        form = ArticlesForm(instance=article)
    return render(request, 'news/update.html', {'form': form, 'article': article})

@login_required
def news_delete(request, id):
    article = Articles.objects.get(id=id)
    if request.user != article.author:
        messages.error(request, 'У вас нет прав для удаления этой статьи.')
        return redirect('news_home')
    article.delete()
    messages.success(request, 'Статья успешно удалена!')
    return redirect('news_home')
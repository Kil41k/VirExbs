from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Articles, ArticleCategory
from .forms import ArticlesForm
from django.views.generic import UpdateView, DeleteView

def index(request):
    return render(request, 'main/home.html')

def create(request):
    if request.method == 'POST':
        form = ArticlesForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:exhibitions')
        else:
            print(form.errors)
    else:
        form = ArticlesForm()
    return render(request, 'main/create.html', {'form': form})

def exhibitions(request, category_id=None):
    if category_id:
        try:
            category = ArticleCategory.objects.get(id=category_id)
            exhibition = Articles.objects.filter(category=category)
        except ArticleCategory.DoesNotExist:
            return HttpResponse("Category does not exist", status=404)
    else:
        exhibition = Articles.objects.all()
    context = {
        'categories': ArticleCategory.objects.all(),
        'exhibition': exhibition,
    }
    return render(request, 'main/exhibition.html', context)

def exhibition_detail(request, id):
    article = get_object_or_404(Articles, id=id)
    return render(request, 'main/exhibition_detail.html', {'article': article})


def exhibition_edit(request, id):
    article = get_object_or_404(Articles, id=id)
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:exhibition_detail', id=article.id)
    else:
        form = ArticlesForm(instance=article)
    return render(request, 'main/exhibition_edit.html', {'form': form, 'article': article})

def exhibition_delete(request, id):
    article = get_object_or_404(Articles, id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:exhibitions')
    return render(request, 'main/exhibition_delete.html', {'article': article})



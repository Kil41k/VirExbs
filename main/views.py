from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Articles, ArticleCategory, Comment
from .forms import ArticlesForm, CommentForm
from django.views.generic.list import ListView
from .mixin.views import TitleMixin


class ExhibitionsView(TitleMixin, ListView):
    model = Articles
    template_name = 'main/index.html'
    paginate_by = 15
    title = 'Exhibitions list'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = ArticleCategory.objects.all()
        return context

#
# class ExbCreateView(TitleMixin, CreateView):
#     model = Articles
#     template_name = 'main/create.html'
#     title = 'Exb Create Page'
#     form_class = ArticlesForm
#

def create(request):
    if request.method == 'POST':
        form = ArticlesForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            exb = form.save(commit=False)
            exb.user = request.user
            exb.save()
            return redirect('articles:home')
        else:
            print(form.errors)
    else:
        form = ArticlesForm()
    return render(request, 'main/create.html', {'form': form})

def exhibition_detail(request, id):
    article = get_object_or_404(Articles, id=id)
    comment = Comment.objects.filter(article=article)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.article = article
            com.user = request.user
            com.save()
        else:
            print(form.errors)
    else:
        form = CommentForm()
    return render(request, 'main/exhibition_detail.html', {'article': article, 'comment': comment, 'form': form})


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



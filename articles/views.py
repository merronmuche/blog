from django.shortcuts import render,HttpResponse
from articles.models import Article
from articles.forms import ArticleForm


def list(request):

    my_articles = Article.objects.all().values()
    context = {
        'my_articles': my_articles
    }
    return render(request, 'article/list.html', context)

def add(request):

    if request.method == 'GET':
        form = ArticleForm()
        context = {
            'form': form
        }

        return render(request, 'article/creat.html', context)
        return render(request,'article/list.html',content)

    else:

        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('created successuflly')

def detail(request,id):
     selected_article = Article.objects.get(id=id)

     data = {
            'article': selected_article,
                }
    
     return render(request, 'article/detail.html', data)
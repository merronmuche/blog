from django.shortcuts import render,HttpResponse
from articles.models import Article
from articles.forms import ArticleForm
def list(request):

    return HttpResponse('list tables are created')

def add(request):

    if request.method == 'GET':
        form = ArticleForm()
        context = {
            'form': form
        }

        return render(request, 'article/creat.html', context)

    else:

        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('created successuflly')
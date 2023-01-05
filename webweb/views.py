from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, '../templates/webweb/main/index.html')

from webweb.models import Article
from django.http import Http404

def index(request):
    context={
        "articles":Article.objects.all()
    }
    return render(request, 'blog/index.html',context)

def index(request):
    if request.method == 'POST':
        article = Article(title=request.POST['title'],body=request.POST['text'])
        article.save()
        return redirect(detail, article.id)

        context = {
            "articles": Article.object.all()
        }
        return render(request, 'Blog/index.html',context)
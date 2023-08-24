from django.shortcuts import render, get_object_or_404
from .models import Article


def home(request):
    published_articles = Article.published_articles.all()
    context = {
        'articles' : published_articles
        }
    return render(request, 'blog/home.html', context = context)

def single_article(request, article):
    article = get_object_or_404(Article, slug=article, status='published')   
    context = {
        'article' : article
        }
    return render(request, 'blog/article.html', context = context)

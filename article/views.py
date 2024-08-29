from django.shortcuts import render
from article.models import Article
from django.core.paginator import Paginator


def index(request):
    articles = Article.objects.order_by('-id')[:4]
    sport_category_articles = Article.objects.filter(category='Game')[:3]
    all_categories = list(set(Article.objects.values_list('category', flat=True)))
    foreign_articles = Article.objects.order_by('id')[:6]
    business_category_articles = Article.objects.filter(category='Business')[:3]
    three_articles = Article.objects.order_by('id')[:6]




    context = {
        'articles': articles,
        'sport_category_articles': sport_category_articles,
        "all_categories": all_categories,
        "foreign_articles": foreign_articles,
        "business_articles": business_category_articles,
        "three_articles": three_articles
    }
    return render(request, 'index.html', context=context)


def categories_page(request):
    cat = request.GET.get("cat")
    all_categories = list(set(Article.objects.values_list('category', flat=True)))

    page = request.GET.get("page")
    paginator = Paginator(Article.objects.filter(category=cat), 2)
    articles_page = paginator.get_page(page)

    articles = Article.objects.filter(category=cat)


    context = {
        "articles": articles,
        "cat": cat,
        "all_categories": all_categories,
        "articles_page": articles_page,
        "page": page
    }
    return render(request, "categories.html", context=context)


def search_articles(request):
    search = request.GET.get("search")
    all_categories = list(set(Article.objects.values_list('category', flat=True)))

    if search:
        articles = Article.objects.filter(title__icontains=search)
    else:
        articles = Article.objects.all()

    context = {
        "articles": articles,
        "all_categories": all_categories
    }
    return render(request, "search_articles.html", context=context)
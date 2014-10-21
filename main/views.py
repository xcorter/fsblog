from django.shortcuts import render
from main.models import Tour, Image, Carousel, Article
from main.forms import ClaimForm

def index(request):
    images = Carousel.objects.all()
    return render(
        request,
        'main/index.html',
        {
            "images": images
        }
    )

def author(request):
    return render(request, 'main/author.html')

def gallery(request):
    images = Image.objects.all()
    return render(
        request,
        'main/gallery.html',
        {
            "images": images
        }
    )

def tours(request):
    tourObjects = Tour.objects.all()
    return render(
        request,
        'main/tours.html',
        {
            "tours": tourObjects
        }
    )

def signUpForATour(request):
    if request.method == "POST":
        form = ClaimForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                'main/messagePage.html',
                {
                    "message": "Спасибо! Ваша заявка была принята, мы свяжимся с вами в ближайшее время."
                }
            )
        else:
            form = ClaimForm()
            return render(
                request,
                'main/signUpForATour.html',
                {
                    "form": form,
                    "error": "Ошибка данных"
                }
            )
    else:
        currentTourId = int(request.GET.get("currentTourId", None))
        tourObjects = Tour.objects.all()
        form = ClaimForm()
        return render(
            request,
            'main/signUpForATour.html',
            {
                "tours": tourObjects,
                "form": form
            }
        )

def articles(request):
    articles = Article.objects.all()
    return render(
        request,
        'main/articles.html',
        {
            "articles": articles
        }
    )

def article(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(
        request,
        'main/article.html',
        {
            "article": article
        }
    )
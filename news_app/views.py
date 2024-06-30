from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Category, News
from .forms import ContactForm
# Create your views here.


def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)
    context = {
        "news_list": news_list
    }
    return render(request, 'news/news_list.html', context=context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news": news
    }
    return render(request, 'news/news_detail.html', context=context)


# def HomePageView(request):
#     categories = Category.objects.all()
#     news_list = News.published.all()[:5]
#     local_one = News.published.filter(category__name='Mahalliy').order_by('-publish_time')[:1]
#     local_news = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[1:6]
#     foreign_one = News.published.filter(category__name='Xorij').order_by('-publish_time')[:1]
#     foreign_news = News.published.all().filter(category__name='Xorij').order_by('-publish_time')[1:6]
#     technology_one = News.published.filter(category__name='Texnologiya').order_by('-publish_time')[:1]
#     technology_news = News.published.all().filter(category__name='Texnologiya').order_by('-publish_time')[1:6]
#     context = {
#         "news_list": news_list,
#         "categories": categories,
#         "local_one": local_one,
#         "local_news": local_news,
#         "foreign_one": foreign_one,
#         "foreign_news": foreign_news,
#         "technology_one": technology_one,
#         "technology_news": technology_news,
#     }
#
#     return render(request, 'news/index.html', context=context)


class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, ** kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by("-publish_time")[:5]
        context['local_news'] = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[1:6]
        context['technology_news'] = News.published.filter(category__name='Texnologiya').order_by('-publish_time')[1:6]
        context['foreign_news'] = News.published.filter(category__name='Xorij').order_by('-publish_time')[1:6]
        context['sport_news'] = News.published.filter(category__name='Sport').order_by('-publish_time')[1:6]
        return context



# def contactPageView(request):
#     print(request.POST)
#     form = ContactForm(request.POST or None)
#
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("Biz bilan bog'langaningiz uchun tashakkur!")
#     context = {
#         "form": form
#     }
#     return render(request, "news/contact.html", context=context)


def page404View(request):
    context = {

    }

    return render(request, "news/404.html", context=context)


def aboutPageView(request):
    context = {

    }

    return render(request, "news/about.html", context=context)


class contactPageView(TemplateView):
    template_name = "news/contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form,
        }

        return render(request, "news/contact.html", context=context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("Sizning xabaringiz saqlandi!")
        context = {
            "form": form,
        }

        return render(request, "news/contact.html", context=context)


class LocalNewsView(ListView):
    model = News
    template_name = "news/local.html"
    context_object_name = "local_news"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Mahalliy')
        return news

class ForeignNewsView(ListView):
    model = News
    template_name = "news/foreign.html"
    context_object_name = "foreign_news"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Xorij')
        return news

class TechnologyNewsView(ListView):
    model = News
    template_name = "news/technology.html"
    context_object_name = "technology_news"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Texnologiya')
        return news


class SportNewsView(ListView):
    model = News
    template_name = "news/sport.html"
    context_object_name = "sport_news"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Sport')
        return news

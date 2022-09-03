from django.shortcuts import render
from .models import NewsPost, Categore, WeeklyTopNews
from django.contrib.auth.decorators import login_required


def index(request):
    data = NewsPost.objects.filter(status ="1").order_by('-date_created').all()
    cata = Categore.objects.all()
    print(cata)
    topnews = NewsPost.objects.filter(status ="1").order_by('-date_created').all()
    news =[]
    for items in cata:
        newsdata = NewsPost.objects.filter(categorie = items).order_by('-date_created').first
        news.append(newsdata)

    return render(request,'app/index.html', {'latest_top':data[:1],
                                            'latest_bottom':data[1:4], 
                                            'data':cata[:6],
                                            'all':data[:6],
                                            'recent':data[:3],
                                            'top_news':topnews[:3],
                                            'news':news
                                            })
    

def categori(request):
    cata = Categore.objects.all()
    news = NewsPost.objects.all()
    return render(request,'app/categori.html', {'data':cata, 'news':news})

def about(request):
    return render(request,'app/about.html')

def latest_news(request):
    return render(request, 'app/latest_news.html')

def contact(request):
    return render(request,'app/contact.html')

def elements(request):
    return render(request, 'app/elements.html')

def blogs(request):
    return render(request, 'app/blog.html')

def detail_blog(request):
    
    return render(request, 'app/single-blog.html')


def details(request, pk):
    data = WeeklyTopNews.objects.get(id= pk)
    # weeklynews = NewsPost.objects.all()
    # if weeklynews.views >=5:
    return render(request, 'app/details.html', {'data':data})    

    
def postdetails(request,pk):
    data = NewsPost.objects.get(id=pk)
    data.views = data.views + 1
    data.save()
    print(data)
    return render(request, 'app/newsdetails.html',{'data':data})

def categorynews(request,pk):
    allcategory = Categore.objects.all()
    category = Categore.objects.get(id=pk)
    categorynews = NewsPost.objects.filter(categorie = category)
    return render(request, 'app/categorynews.html', {'relatednews':categorynews[:6],'data':allcategory})
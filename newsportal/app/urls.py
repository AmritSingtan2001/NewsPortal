from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('categori', views.categori, name='cagetori'),
    path('about', views.about, name='about'),
    path('latest', views.latest_news, name='latest'),
    path('contact', views.contact, name='contact'),
    path('element', views.elements, name='element'),
    path('blog', views.blogs, name='blog'),
    path('detailblog', views.detail_blog, name='detailblog'),
    path('details<int:pk>', views.details, name='details'),
    path('details/post/<int:pk>', views.postdetails, name='post'),
    path('categori/relatednews/<int:pk>', views.categorynews, name='category')


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

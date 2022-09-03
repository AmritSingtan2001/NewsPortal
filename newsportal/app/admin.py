from django.contrib import admin
from . models import NewsPost, Categore, WeeklyTopNews

class NewCategory(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Categore, NewCategory)



class NewAdmin(admin.ModelAdmin):
    list_display = ('id','categorie','headline','short_description','content','images','reporter','date_created','date_updated','status','views')

admin.site.register(NewsPost, NewAdmin)

class WeeklyNewsAdmin(admin.ModelAdmin):
    list_display = ('id','type','headline','short_description','details','images','reporter','date_created','date_updated','status')

admin.site.register(WeeklyTopNews, WeeklyNewsAdmin)


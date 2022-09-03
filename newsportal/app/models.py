from django.db import models


categori = (
    ("General","General"),
    ("Lifestyle","Lifestyle"),
    ("Travel","Travel"),
    ("Fashion","Fashion"),
    ("Sports","Sports"),
    ("Technology","Technology")
)

class Categore(models.Model):
    name = models.CharField(choices= categori, default= "General", max_length=50)

    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.name

status = (
    ('1', "Published"),
    ('2', "Unpublished")
)

class NewsPost(models.Model):
    categorie = models.ForeignKey(Categore, on_delete= models.CASCADE, related_name="cata")
    headline = models.TextField()
    short_description = models.TextField()
    content = models.TextField()
    images = models.ImageField(upload_to ='newsimage')
    reporter = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now= True)
    date_updated = models.DateTimeField(auto_now = True)
    status = models.CharField(choices=status, default="2", max_length=50)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-id',]
    
    def __str__(self):
        return self.headline

class WeeklyTopNews(models.Model):
    type = models.ForeignKey(Categore, on_delete= models.CASCADE, related_name='category')
    headline = models.TextField()
    short_description = models.TextField()
    details = models.TextField()
    images = models.ImageField(upload_to ='newsimage')
    reporter = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now= True)
    date_updated = models.DateTimeField(auto_now = True)
    status = models.CharField(choices=status, default="2", max_length=50)

    class Meta:
        ordering = ['-id',]
    
    def __str__(self):
        return self.headline + self.short_description 

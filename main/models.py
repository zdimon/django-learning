from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='news',null=True, blank=True)
    def __str__(self):
        return self.title

class Comment(models.Model): 
    text = models.TextField()
    author = models.CharField(max_length=250)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    


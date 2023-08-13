from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default='default.png', blank = True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    
    def __str__(self):
      return self.title
    def snippet(self):
       return self.body[:50] + "..."

# python manage.py makemigrations
# python manage.py migrate



# ORM  interacting with database
# >>> from articles.models import Article
# >>> Article
# <class 'articles.models.Article'>
# >>> Article.objects.all()
# <QuerySet []>
# >>> article = Article()
# >>> article
# <Article: Article object (None)>
# >>> article.title = "hello ninja"
# >>> artice.title
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'artice' is not defined
# >>> article.title 
# 'hello ninja'
# >>> article.save()
# >>> Article.objects.all()
# <QuerySet [<Article: Article object (1)>]>
# >>> Article.objects.all()[0]
# <Article: Article object (1)>
# >>> Article.objects.all()[0].title
# 'hello ninja'
# >>>
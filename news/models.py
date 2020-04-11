from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='news/',null=True,blank=True)
    date = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'news'


from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=78, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(max_length=1000, null=False)
    def __str__(self):
       return self.name
class AboutUs(models.Model):
    heading = models.CharField(max_length=255, null=False)
    description = HTMLField()
    def __str__(self):
        return self.heading
class Category(models.Model):
    Event = models.CharField(max_length=255,null=False)
    def __str__(self):
        return self.Event
class Blog(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    writter = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    details = HTMLField()
    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = HTMLField()
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField()
    contact = models.IntegerField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name

class CustomOrders(models.Model):
    comment = HTMLField()
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField()
    contact = models.IntegerField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name


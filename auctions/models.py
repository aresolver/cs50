from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.id} es {self.name}"

#class for auction listings
class Article(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField() 
    starting_bid = models.FloatField() 
    current_price = models.FloatField() 
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="by_category")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="by_user")
    url_image = models.URLField(max_length=250)

    def __str__(self):
        return f"{self.name}"

class Bid(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="bids_by_article")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids_by_user")
    price = models.FloatField()
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.article} ({self.user})"

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments_by_article")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_by_user") 
    description = models.TextField()       
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} : {self.article} to {self.user}"

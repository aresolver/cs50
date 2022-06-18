from django.contrib import admin
from .models import User
from .models import Category
from .models import Article
from .models import Bid, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Bid)
admin.site.register(Comment)

from django.contrib import admin
from .models import User, Bid, AuctionListing, Comment, Category

# Register your models here.
admin.site.register(User)
admin.site.register(AuctionListing)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Category)
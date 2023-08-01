from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    def __str__(self):
        return f"User: {self.username}"
    
class Category(models.Model):
    categoryType = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.categoryType}"

class AuctionListing(models.Model):
    item_name = models.CharField(max_length=64, default="No Name")
    item_description = models.CharField(max_length=600, default="No Description")
    date_created = models.DateTimeField(auto_now_add=True)
    imageURL = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="listings", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inventory", null=True)
    potentialBuyers = models.ManyToManyField(User, related_name="watchlist")
    openListing = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.item_name}"

class Bid(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=7)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids", null=True)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="bids", null=True)
    
    def __str__(self):
        return f"Bid Price: {self.price}"
    
class Comment(models.Model):
    text = models.CharField(max_length=600, blank=True)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="comments", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments", null=True)

    def __str__(self):
        return f"Text: {self.text}"
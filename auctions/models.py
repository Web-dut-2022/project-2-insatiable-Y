from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Listing(models.Model):
    seller = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    category = models.CharField(max_length=64, default=None)
    starting_bid = models.IntegerField(default=0)
    URL = models.CharField(max_length=200, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Bid(models.Model):
    user = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    listingid = models.IntegerField()
    bid = models.IntegerField()

class Comment(models.Model):
    user = models.CharField(max_length=64)
    comment = models.CharField(max_length=1000)
    listingid = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Watchlist(models.Model):
    user = models.CharField(max_length=64)
    listingid = models.IntegerField()

class Winner(models.Model):
    owner = models.CharField(max_length=64)
    winner = models.CharField(max_length=64)
    listingid = models.IntegerField()
    winprice = models.IntegerField()
    title = models.CharField(max_length=64, null=True)

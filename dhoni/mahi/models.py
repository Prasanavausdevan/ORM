
from django.db import models
from django.contrib import admin
class football_players (models.Model):
    name=models.CharField(max_length=20)
    dob= models.IntegerField()
    jersey_no=models.IntegerField()
    height=models.IntegerField()
    weight=models.IntegerField()
    country=models.CharField(max_length=100)

class football_playersAdmin (admin.ModelAdmin):
    list_display=["name","dob","jersey_no","height","weight","country"]

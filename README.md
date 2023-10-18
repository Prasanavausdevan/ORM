# Ex02 Django ORM Web Application
## Date: 18/10/2023

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```
admin.py
from django.contrib import admin
from.models import football_players,football_playersAdmin
admin.site.register(football_players,football_playersAdmin)
model.py
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

```
## OUTPUT
![Alt text](<Screenshot (2).png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully

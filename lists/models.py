from django.db import models
class List(models.Model):
    caption = models.TextField(default='To Do List')
class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List,default=None)

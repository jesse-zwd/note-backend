from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Notebook(models.Model):
    name = models.CharField(max_length=100, default='', verbose_name='name')
    user = models.ForeignKey(User, related_name='notebooks', verbose_name='user', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=datetime.now, verbose_name='createdAt')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'notebooks'
        verbose_name_plural = verbose_name


class Note(models.Model):
    title = models.CharField(max_length=100, default='', verbose_name='title')
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name='description')
    cover = models.CharField(max_length=200, null=True, blank=True, verbose_name='cover')
    data = models.CharField(max_length=200, default='', verbose_name='data')
    notebook = models.ForeignKey(Notebook, related_name='notes', verbose_name='notebook', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=datetime.now, verbose_name='createdAt')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'note'
        verbose_name_plural = verbose_name
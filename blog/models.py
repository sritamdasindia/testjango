# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BlogEntry(models.Model):
    text = models.TextField()
    timestamp = models.DateField()

    def __str__(self):
        return str(self.text)

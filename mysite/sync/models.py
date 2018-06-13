from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class Participant(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    siblings = models.CharField(max_length=200)
    exposures = models.CharField(max_length=200,default='None')
    mutations = models.CharField(max_length=200,default='None')
    status = models.CharField(max_length=200,default='Not Reviewed')

    def __str__(self):
        return self.name

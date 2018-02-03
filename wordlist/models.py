# This is an auto-generated Django model module.
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Word(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    word = models.CharField(max_length=255, blank=True, null=True)
    pronounciation = models.CharField(max_length=255, blank=True, null=True)
    translation = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'words'

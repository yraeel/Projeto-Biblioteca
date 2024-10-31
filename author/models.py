import uuid
from django.db import models

# Create your models here.

class Autor(models.Model):

    id_autor = models.AutoField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    author_name = models.CharField(max_length=254, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
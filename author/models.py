import uuid
from django.db import models

# Create your models here.

class Author(models.Model):

    id_author = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    author_name = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
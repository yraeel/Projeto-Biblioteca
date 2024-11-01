import uuid
from django.db import models

# Create your models here.

class Author(models.Model):

    id_author = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    author_name = models.CharField(max_length=254, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        managed = True
        db_table = 'author'

    
    def __str__(self) -> str:
        return self.author_name
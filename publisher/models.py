import uuid
from django.db import models
from author.models import Author

# Create your models here.

class Publisher(models.Model):

    id_publisher = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    publisher_name = models.CharField(max_length=254, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ManyToManyField(Author, related_name='publisher')
    # adicionar chave estrangeira Livro


    class Meta:
        managed = True
        db_table = 'publisher'

    
    def __str__(self) -> str:
        return self.publisher_name



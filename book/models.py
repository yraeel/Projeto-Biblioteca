import uuid
from django.db import models
from author.models import Author
from publisher.models import Publisher


class Book(models.Model):

    id_book = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    book_name = models.CharField(max_length=254, blank=False)
    pages = models.IntegerField()
    edition = models.IntegerField()
    language = models.CharField(max_length=50, blank=False)
    release = models.IntegerField()
    country = models.CharField(max_length=50)

    fk_author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    fk_publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name='books')



    class Meta:
        managed = True
        db_table = 'books'

    
    def __str__(self) -> str:
        return f"{self.book_name} - {self.fk_author} - {self.fk_publisher}"



from django.db import models

# Create your models here.
class Books(models.Model):
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=150)

    def __str__(self):
        return self.book_name
    
    class Meta:
        verbose_name_plural = 'Books'
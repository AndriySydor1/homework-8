from django.db import models
from authors.models import Author

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.text[:50]  # Показати перші 50 символів цитати для зручності

    def get_tags(self):
        return self.tags.split(',')

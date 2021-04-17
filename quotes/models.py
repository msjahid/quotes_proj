from django.db import models


# Create your models here.

class QuoteCategory(models.Model):
    title = models.CharField(max_length=65)

    def __str__(self):
        return self.title[:50]


class Quote(models.Model):
    quotes = models.TextField()
    author = models.CharField(max_length=150)
    quoteCategory = models.ForeignKey('QuoteCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.quotes[:50]
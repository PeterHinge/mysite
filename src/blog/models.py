from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Article(models.Model):

    objects = models.Manager()
    published_articles = PublishedManager()
    
    options = (
    ('draft', 'Draft'),
    ('ready', 'Ready'),
    ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='published_date')
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='articles')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')

    class Meta:
        ordering = ('-published_date',)

    def get_url(self):
        return '/blog/article/' + self.slug

    def __str__(self):
        return self.title
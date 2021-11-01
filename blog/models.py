from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category        = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title           = models.CharField(max_length=250)
    excerpt         = models.TextField(null=True)
    slug            = models.SlugField(max_length=250, unique_for_date='publish')
    publish         = models.DateTimeField(default=timezone.now)
    author          = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content         = models.TextField()
    status          = models.CharField(max_length=10, choices=options, default='draft')

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")
        ordering = ('-publish',)

        def __str__(self):
            return self.title
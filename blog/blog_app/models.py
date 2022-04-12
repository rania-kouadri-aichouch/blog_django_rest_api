from django.db import models
from django.db.utils import IntegrityError
from django.utils.crypto import get_random_string
from shared.slugify import slugify

from django.conf import settings


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=300)
    description=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Blog category'
        verbose_name_plural = 'Blog categories'
        db_table = 'blog_categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=300)
    category = models.ForeignKey(
        to=Category,
        related_name='posts',
        on_delete=models.CASCADE
    )
    content = models.TextField()
    image = models.ImageField(upload_to='images/blog', default='images/blog/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        db_table = 'blog_posts'

    def __str__(self):
        return self.title

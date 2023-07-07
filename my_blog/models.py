from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='my_home/products/', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    blog_views = models.IntegerField(verbose_name="blog_views", default=0)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='artilce_image/')
    description = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
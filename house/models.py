from django.db import models



class Category(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               related_name='children',
                               blank=True, null=True)

    def __str__(self):
        if self.parent:
            return f'{self.parent}-->{self.name}'
        return self.name


class Advantages(models.Model):
    title = models.CharField(max_length=200,)
    image = models.ImageField(upload_to='advantages', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title



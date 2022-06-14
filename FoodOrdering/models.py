from django.urls import reverse
from django.db import models
import os


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category',
                       args=[self.slug])

    def real_product(self):
        return reverse('app_activities:admin_product_list_by_category',
                       args=[self.slug])


def food_image(instance, filename):
    upload_to = 'media/'
    if instance.id:
        filename = 'foods/{}'.format(instance.category.name)
    return os.path.join(upload_to, filename)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to=food_image, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def real_product(self):
        return reverse('app_activities:admin_product_detail',
                       args=[self.id, self.slug])

    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.id, self.slug])


    def __str__(self):
        return self.name

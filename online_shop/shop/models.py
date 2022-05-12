from django.urls import reverse
from django.db import models
from django.utils import timezone
# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.contrib.auth.models import User


class Product(models.Model):
    """Represents info about product"""
    name = models.CharField('Название товара', max_length=100)
    description = models.TextField('Описание', max_length=4000)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    weight = models.DecimalField(max_digits=15, decimal_places=3)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    category = models.ForeignKey('Categories', null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(editable=False, default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    image = models.ForeignKey('ProductImages', blank=True, null=True, on_delete=models.CASCADE)
    # reviews
    # comments = models.ManyToManyField(User)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    """class that represents images of products"""
    image = models.ImageField('Фото товаров', null=True, blank=True)

    class Meta:
        verbose_name = 'Изображения товаров'
        verbose_name_plural = 'Изображения товаров'

    def __str__(self):
        return self.product


class Categories(models.Model):
    """Class that represents different categories to choose"""
    category = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товара'
        ordering = ('category',)

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.category


# class Profile(models.Model):
#     """Represents profile info about user"""
#     user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
# #   taking info from django User class

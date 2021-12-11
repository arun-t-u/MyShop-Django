from django.db import models
from django.db.models.deletion import CASCADE
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug         = models.SlugField(max_length=200, unique=True)
    description  = models.TextField(max_length=500, blank=True)
    price        = models.IntegerField()
    image        = models.ImageField(upload_to='photo/Products/%y/%m/%d')
    stock        = models.IntegerField()
    is_avilable  = models.BooleanField(default=True)
    category     = models.ForeignKey(Category, on_delete=CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date= models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
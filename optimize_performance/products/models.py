from django.db import models


class ProductTag(models.Model):
    name = models.CharField(verbose_name='タグ名', max_length=100)


class ProductBrand(models.Model):
    name = models.CharField('ブランド名', max_length=100)


class Product(models.Model):
    name = models.CharField(verbose_name='製品名', max_length=100)
    tags = models.ManyToManyField('ProductTag', verbose_name='タグ')
    brand = models.ForeignKey('ProductBrand', on_delete=models.PROTECT, blank=True, null=True)

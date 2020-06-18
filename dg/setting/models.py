from django.db import models

# Create your models here.
class Brand(models.Model):
    BRDName=models.CharField(verbose_name='brand name',max_length=40)
    BRDDesc=models.TextField(verbose_name='brand description',blank=True,null=True)
    class Meta:
        verbose_name=('Brand')
        verbose_name_plural=('Brands')
    def __str__(self):
        return  self.BRDName


class Variant(models.Model):
    VarName=models.CharField(verbose_name='variant name',max_length=40)
    VarDesc=models.TextField(verbose_name='variant description',blank=True,null=True)
    class Meta:
        verbose_name=('Variant')
        verbose_name_plural=('Variants')
    def __str__(self):
        return  self.VarName


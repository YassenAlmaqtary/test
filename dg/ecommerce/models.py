from django.db import models
from django.utils import translation as _

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from  django.conf import settings

# Create your models here.


class Product(models.Model):
    proName = models.CharField(verbose_name='product Name', max_length=200)
    proCategory=models.ForeignKey(verbose_name='category',to='Category',on_delete=models.CASCADE,blank=True,null=True)
    proBrand=models.ForeignKey(verbose_name='brand',to='setting.Brand',on_delete=models.CASCADE,blank=True,null=True)
    proDesc = models.TextField(verbose_name='product Description')
    proIImag = models.ImageField(verbose_name='image', upload_to='Porduct/',blank=True,null=True)
    proPrice = models.DecimalField(verbose_name='product price', max_digits=5, decimal_places=2)
    proCost = models.DecimalField(verbose_name='product Cost', max_digits=5, decimal_places=2)
    slug = models.SlugField(max_length = 250, blank = True, null = True)
    proCreated=models.DateTimeField(verbose_name='product Created')

    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products "

    def __str__(self):
        return self.proName




class ProductImag(models.Model):
    PRDIproduct = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    PRDIImag = models.ImageField(verbose_name='image', upload_to='Porduct/')
    class Meta:

        verbose_name="ProductImag "
        verbose_name_plural="ProductImages "
    def __str__(self):
        pass
        return str(self.PRDIImag)




class Category(models.Model):
    CatMain_Category = models.CharField(verbose_name='Main Category',max_length=50)
    CatParent=models.ForeignKey(verbose_name='Category Parent',to='self',on_delete=models.CASCADE,limit_choices_to={'CatParent__isnull':True},blank=True,null=True)
    CatDesc=models.TextField(verbose_name='Description')
    CatImage_Category=models.ImageField(verbose_name='Image',upload_to='category/')
    class Meta:
        verbose_name="Category "
        verbose_name_plural="Categores "
    def __str__(self):
        return self.CatMain_Category





class Product_Alternative(models.Model):

    PALNProduct=models.ForeignKey(to=Product,on_delete=models.CASCADE,related_name='main_Product',verbose_name='product')
    PALNAlternative=models.ManyToManyField(to=Product,related_name='alternative_product',verbose_name='alternative')
    class Meta:
        verbose_name="Product_Alternative "
        verbose_name_plural="Product_Alternatives"
    def __str__(self):

        return str(self.PALNAlternative)



class Product_Accessories(models.Model):

    PACCproduct=models.ForeignKey(to=Product,on_delete=models.CASCADE,related_name='mainAccessory_Product',verbose_name='Product')
    PACCAccessories=models.ManyToManyField(to=Product,related_name='accessories_product',verbose_name='accessories')
    class Meta:
        verbose_name="Product_Accessory "
        verbose_name_plural="Product_Accessories"
    def __str__(self):
        return str(self.PACCproduct)



class Profile(models.Model):
    user=models.OneToOneField(to=User,verbose_name='user',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='ProFile/',blank=True,null=True)
    country=CountryField()
    address=models.CharField(max_length=100,blank=True,null=True)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    bio = models.TextField()
    def __unicode__(self):
         return u"%s" % self.user
    def __str__(self):
        return self.user.username




@receiver(post_save,sender=User)
def update_profile_signal(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()



class CartProduct(models.Model):
       user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
       CP_isorder=models.BooleanField(default=False)
       C_Product=models.ForeignKey(to=Product,on_delete=models.CASCADE,verbose_name='product')
       C_ip=models.CharField(max_length=255,verbose_name='ipaddress',blank=True,null=True)
       C_Quantity=models.IntegerField(default=1,verbose_name='quantity')
       def __str__(self):
        return f"{self.C_Quantity}of{self.C_Product.proName}"


class Cart(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    C_Products=models.ManyToManyField(to=CartProduct,verbose_name='Products')
    C_StartDate=models.DateTimeField(auto_now_add=True)
    C_order_date=models.DateTimeField()
    C_isorder=models.BooleanField(default=False)
    def __str__(self):
        return self.user.username








from .models import Product
from rest_framework import  serializers




class PostSerializer(serializers.ModelSerializer):
     class Meta:
         model =Product
         #fields= '__all__'
         fields = ('proName', 'proCategory', 'proBrand','proDesc','proIImag','proPrice','proCost','slug','proCreated')

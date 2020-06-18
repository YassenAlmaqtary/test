
from django.urls import path,include
from .import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('product', views.Proapi)
urlpatterns=[
             path('',views.product_List,name='index'),
             #path('',views.pagination.as_view,name='index'),
             path('<int:id>/',views.product_ditele,name='product_ditele'),
             path('search',views.search,name='search'),
             path('signup',views.singup,name='signup'),
             path('profile/<slug:slug>/',views.ShowProfile,name='ShowProfile'),
             path('profile/',views.ShowProfile,name='ShowProfile'),
             path('addcart/<slug:slug>',views.add_to_cart,name="add_to_cart"),
             path('removecart/<slug:slug>',views.remove_to_cart,name="remove_to_cart"),
             path('profile_updet/',views.ge_edtProfle,name='ge_edtProfle'),
             path('change_password/',views.get_password_change,name='get_password_change'),
             path('', include(router.urls)),
             path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),

             ]




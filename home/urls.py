from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views
admin.site.site_header="Login to Developer"

urlpatterns = [
    path('', views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/', views.contact, name='contact'),
    # path('sucess', views.success, name='success'),
    path('product_page/', views.product, name='product'),
    path('user_login/', views.handlelogin, name='handlelogin'),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('testdrive', views.testdrives, name='testdrives'),
    path('ProductDetails/',views.Details,name='Details'),
    path('Cart/', views.cart, name='cart'),
    path('Profile/', views.myprofile, name='myprofile'),
    # path('C_Pro/', views.chngpro, name='chngpro'),
    path('Register/', views.register, name='register'),
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('inc/', views.increase, name='increase'),
    path('dec/', views.decrease, name='decrease'),
    path('remove/', views.remove_from_cart, name='remove_from_cart'),
    path('for_checkout', views.checkout, name='checkout'),
    path('orderplace',views.place,name='place'),
    path('orderdetail', views.myorder, name='myorder'),
    # path('remove_after_order/', views.remove_after_checkout, name='remove_after_checkout'),
    path('Prod_link', views.prod_link, name='prod_link'),
    path('edit_profile/', views.profile_edit, name='profile_edit'),
]
from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.home),
    # path('login/',views.login.view,name='login'),
    path('index/', views.index_page, name='index'),
    path('nike/', views.nike_page, name='nike'),
    path('adidas/', views.adidas_page, name='adidas'),
    path('puma/', views.puma_page, name='puma'),
    path('converse/', views.converse_page, name='converse'),
    path('onitsukaTiger/', views.OnitsukaTiger_page, name='onitsukaTiger'),
    path('allpro/', views.allpro_page, name='allpro'),
    path('productadd/', views.productadd, name='ProductAdd')
]

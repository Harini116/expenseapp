from myapp import views
from django.urls import path

urlpatterns = [
    path('about', views.index),
    path('addexpense', views.indexexp),
    path('myexpense', views.indexmyexp),
    ]
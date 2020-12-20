
from django.contrib import admin
from django.urls import path
from blog.views import index,contact,about,detaill
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="index"),
    path('contact/',contact,name="contact" ),
    path('about/', about, name="about"),
    path('detaill/',detaill,name="detaill"),
]

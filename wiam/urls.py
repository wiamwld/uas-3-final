
from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog),
    path('Send_contact/', Send_contact, name='Send_contact'),
]

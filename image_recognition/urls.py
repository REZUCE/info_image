from django.urls import path
from .views import image

app_name = 'image_recognition'
urlpatterns = [
    path('', image, name='image')
]

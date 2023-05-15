# urls.py


from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ImageList

urlpatterns = [
    path('images/', ImageList.as_view(), name='image-list'),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)




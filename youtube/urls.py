from django.urls import path
from . import views
app_name = 'youtube'
urlpatterns = [
    path('' , views.download , name = 'youtube'),
]